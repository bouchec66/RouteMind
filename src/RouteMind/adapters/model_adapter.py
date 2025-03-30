# src/RouteMind/adapters/model_adapter.py

import requests

class ModelAdapter:
    def __init__(self, name, endpoint=None):
        self.name = name
        self.endpoint = endpoint  # Used for HTTP API models

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Each adapter must implement 'generate'.")


class MistralAdapter(ModelAdapter):
    def generate(self, prompt: str) -> str:
        if not self.endpoint:
            raise ValueError("MistralAdapter requires an endpoint URL.")

        payload = {
            "prompt": prompt,
            "max_new_tokens": 200,
            "temperature": 0.7,
        }

        response = requests.post(f"{self.endpoint}/api/v1/generate", json=payload)
        result = response.json()
        return result["results"][0]["text"].strip()


class GPT4Adapter(ModelAdapter):
    def generate(self, prompt: str) -> str:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")

        chat = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[{"role": "user", "content": prompt}]
        )
        return chat.choices[0].message["content"].strip()


# Factory function

def get_model_adapter(model_name: str) -> ModelAdapter:
    model_name = model_name.lower()

    if model_name == "mistral-7b":
        return MistralAdapter(name="mistral-7b", endpoint="http://localhost:5000")

    elif model_name == "gpt-4":
        return GPT4Adapter(name="gpt-4")

    else:
        raise ValueError(f"Unknown model: {model_name}")
