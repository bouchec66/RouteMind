# tests/test_chatbot.py

from utils.chatbot import chat_with_openai

def test_chat_with_openai():
    api_key = "your_openai_api_key"
    prompt = "Hello, how are you?"
    response = chat_with_openai(prompt, api_key)
    assert isinstance(response, str)
    assert len(response) > 0

