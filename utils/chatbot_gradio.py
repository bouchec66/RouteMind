# src/energy_aware_models/utils/chatbot_gradio.py

import gradio as gr
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

def respond(message, api_key):
    return chat_with_openai(message, api_key)

def launch_gradio_chatbot(api_key):
    iface = gr.Interface(
        fn=lambda message: respond(message, api_key),
        inputs="text",
        outputs="text",
        title="Chatbot Interface",
        description="Interact with the chatbot powered by OpenAI."
    )
    iface.launch()

