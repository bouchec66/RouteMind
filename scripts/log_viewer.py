# scripts/log_viewer.py

import argparse
import json
import os
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


def main():
    parser = argparse.ArgumentParser(description="View and filter RouteMind chain logs")
    parser.add_argument("--logfile", default="logs/chain_log.jsonl", help="Path to the log file")
    parser.add_argument("--limit", type=int, default=5, help="How many entries to display")
    parser.add_argument("--search", help="Keyword to filter by input/output")

    args = parser.parse_args()

    logs = load_logs(args.logfile)

    if args.search:
        logs = [l for l in logs if args.search.lower() in l["input"].lower() or args.search.lower() in l["output"].lower()]

    if not logs:
        print("No matching log entries found.")
        return

    print(f"\n📂 Showing latest {min(args.limit, len(logs))} entries from: {args.logfile}")

    for i, entry in enumerate(reversed(logs[-args.limit:])):
        display_entry(entry, i)


if __name__ == "__main__":
    main()
