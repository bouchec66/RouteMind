# src/energy_aware_models/utils/api_tester.py

import openai

def test_openai_api_key(api_key):
    """
    Tests the provided OpenAI API key by making a simple request.
    """
    try:
        openai.api_key = api_key
        openai.Engine.list()
        print("OpenAI API key is valid.")
    except Exception as e:
        print(f"Invalid OpenAI API key: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test OpenAI API Key")
    parser.add_argument("--api_key", required=True, help="OpenAI API Key")
    args = parser.parse_args()

    test_openai_api_key(args.api_key)

