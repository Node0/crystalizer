# ./backends/providers/openai.py
from . import register_provider
from typing import Dict, Any
import requests
from utilities import Print

class OpenAIProvider:
    def __init__(self, config: Dict[str, Any]):
        self.api_key = config.get("api_key")
        self.model = config.get("model", "gpt-4o-mini")
        self.base_url = config.get("base_url", "https://api.openai.com/v1")
        self.max_tokens = config.get("max_tokens", 1500)
        self.temperature = config.get("temperature", 0.1)

        if not self.api_key:
            Print("FAILURE", "OpenAI API key required in config")
            raise ValueError("OpenAI API key required in config")

    def generate(self, system_prompt: str, user_content: str) -> str:
        # Implementation remains unchanged
        ...

@register_provider("openai")
class OpenAIProviderFactory:
    @staticmethod
    def create(config: dict):
        return OpenAIProvider(config)
