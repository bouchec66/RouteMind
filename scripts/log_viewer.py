# scripts/log_viewer.py

import argparse
import json
import os
import csv
from datetime import datetime

def load_logs(filepath):
    if not os.path.exists(filepath):
        print(f"❌ Log file not found: {filepath}")
        return []
    with open(filepath, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def display_entry(entry, index):
    print("\n-------------------------------")
    print(f"🔹 Entry #{index + 1} | {entry['timestamp']}")
    print(f"📄 Config: {entry['config']}")
    print(f"📝 Input: {entry['input']}")
    print(f"💡 Output: {entry['output']}")

def export_to_csv(logs, csv_path):
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['timestamp', 'input', 'output', 'config']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in logs:
            writer.writerow({
                'timestamp': entry['timestamp'],
                'input': entry['input'],
                'output': entry['output'],
                'config': entry['config']
            })
    print(f"✅ Exported {len(logs)} entries to {csv_path}")

def main():
    parser = argparse.ArgumentParser(description="View and filter RouteMind chain logs")
    parser.add_argument("--logfile", default="logs/chain_log.jsonl", help="Path to the log file")
    parser.add_argument("--limit", type=int, default=5, help="How many entries to display")
    parser.add_argument("--search", help="Keyword to filter by input/output")
    parser.add_argument("--config", help="Filter by config file used")
    parser.add_argument("--export", help="Path to export results as CSV")
    parser.add_argument("--sort", choices=["asc", "desc"], default="desc", help="Sort order by timestamp")

    args = parser.parse_args()

    logs = load_logs(args.logfile)

    if args.search:
        logs = [l for l in logs if args.search.lower() in l["input"].lower() or args.search.lower() in l["output"].lower()]

    if args.config:
        logs = [l for l in logs if args.config in l["config"]]

    if args.sort == "asc":
        logs = sorted(logs, key=lambda x: x["timestamp"])
    else:
        logs = sorted(logs, key=lambda x: x["timestamp"], reverse=True)

    if args.export:
        export_to_csv(logs, args.export)
        return

    if not logs:
        print("No matching log entries found.")
        return

    print(f"\n📂 Showing latest {min(args.limit, len(logs))} entries from: {args.logfile}")

    for i, entry in enumerate(logs[:args.limit]):
        display_entry(entry, i)


if __name__ == "__main__":
    main()
