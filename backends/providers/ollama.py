# ./backends/providers/ollama.py
from . import register_provider
from typing import Dict, Any
import requests
from utilities import Print

class OllamaProvider:
    def __init__(self, config: Dict[str, Any]):
        self.host = config.get("host", "localhost")
        self.port = config.get("port", 11434)
        self.model = config.get("model", "qwen2.5-coder:32b")
        self.base_url = f"http://{self.host}:{self.port}"
        self.options = config.get("options", {})

    def generate(self, system_prompt: str, user_content: str) -> str:
        # Implementation remains unchanged
        ...

@register_provider("ollama")
class OllamaProviderFactory:
    @staticmethod
    def create(config: dict):
        return OllamaProvider(config)
