# src/energy_aware_models/utils/chatbot.py

import openai

def chat_with_openai(prompt, api_key):
    """
    Sends a prompt to the OpenAI API and returns the response.
    """
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CLI Chatbot using OpenAI API")
    parser.add_argument("--api_key", required=True, help="OpenAI API Key")
    args = parser.parse_args()

    print("Chatbot initialized. Type 'exit' to end the session.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chat_with_openai(user_input, args.api_key)
        print(f"Bot: {response}")

