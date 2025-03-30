# scripts/run_chain.py

import sys
import os
import datetime
import json

# Make sure we can import from src if running from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from RouteMind.engine.chain_runner import ChainRunner


def log_interaction(input_text, output_text, config_path, logfile):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "input": input_text,
        "output": output_text,
        "config": config_path
    }
    log_dir = os.path.dirname(logfile)
    os.makedirs(log_dir, exist_ok=True)

    with open(logfile, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Run a RouteMind LLM chaining config")
    parser.add_argument("--config", required=True, help="Path to chain config YAML file")
    parser.add_argument("--input", required=True, help="Prompt to run through the chain")
    parser.add_argument("--logfile", default="logs/chain_log.jsonl", help="Path to output log file")
    parser.add_argument("--dry-run", action="store_true", help="Run chain without calling actual models")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output of each step")

    args = parser.parse_args()

    runner = ChainRunner(config_path=args.config)

    if args.dry_run:
        print("[DRY RUN] Skipping actual model calls. Exiting.")
        return

    result = runner.run(prompt=args.input)

    if args.verbose:
        print("\n[VERBOSE] Final Output:")
    print("\n🧠 Final Output:")
    print(result)

    log_interaction(args.input, result, args.config, args.logfile)


if __name__ == "__main__":
    main()
