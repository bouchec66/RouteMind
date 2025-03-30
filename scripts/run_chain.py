# scripts/run_chain.py

import sys
import os

# Make sure we can import from src if running from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from RouteMind.engine.chain_runner import ChainRunner


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Run a RouteMind LLM chaining config")
    parser.add_argument("--config", required=True, help="Path to chain config YAML file")
    parser.add_argument("--input", required=True, help="Prompt to run through the chain")

    args = parser.parse_args()

    runner = ChainRunner(config_path=args.config)
    result = runner.run(prompt=args.input)
    print("\n🧠 Final Output:")
    print(result)


if __name__ == "__main__":
    main()
