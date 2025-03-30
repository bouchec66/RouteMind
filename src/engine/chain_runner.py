import yaml
import re

# Placeholder adapters (you'll fill these in later)
from adapters.model_adapter import get_model_adapter  # factory function you will define

class ChainStep:
    def __init__(self, name, model_name, fallback_conditions):
        self.name = name
        self.model = get_model_adapter(model_name)
        self.fallback_conditions = fallback_conditions or []

    def should_fallback(self, response: str) -> bool:
        if not self.fallback_conditions:
            return False

        for rule in self.fallback_conditions:
            if isinstance(rule, dict):
                if 'response_length_lt' in rule:
                    if len(response) < rule['response_length_lt']:
                        return True
                if 'contains_any' in rule:
                    if any(phrase.lower() in response.lower() for phrase in rule['contains_any']):
                        return True
        return False

    def run(self, prompt):
        print(f"Running step: {self.name} with model: {self.model.name}")
        response = self.model.generate(prompt)
        return response

class ChainRunner:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        self.steps = []
        for step_cfg in config['steps']:
            step = ChainStep(
                name=step_cfg['name'],
                model_name=step_cfg['model'],
                fallback_conditions=step_cfg.get('fallback_if')
            )
            self.steps.append(step)

    def run(self, prompt):
        for i, step in enumerate(self.steps):
            response = step.run(prompt)
            if i == len(self.steps) - 1 or not step.should_fallback(response):
                print(f"\n✅ Final output from step '{step.name}':\n{response}\n")
                return response
            else:
                print(f"⚠️ Fallback triggered at step '{step.name}' → moving to next step\n")
        return None

# Example CLI usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python chain_runner.py <config.yaml> \"<input prompt>\"")
        exit(1)

    config_path = sys.argv[1]
    input_text = sys.argv[2]
    runner = ChainRunner(config_path)
    runner.run(input_text)
