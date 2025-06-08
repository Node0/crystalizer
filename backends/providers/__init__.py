# ./backends/providers/__init__.py
# Factory registration
from typing import Dict, Type
from abc import ABC

PROVIDER_REGISTRY: Dict[str, Type["LLMProvider"]] = {}

def register_provider(name: str):
    def decorator(cls):
        if not issubclass(cls, LLMProvider):
            raise TypeError("Registered class must inherit from LLMProvider")
        if name in PROVIDER_REGISTRY:
            raise ValueError(f"Provider {name} already registered")
        PROVIDER_REGISTRY[name] = cls
        return cls
    return decorator

def get_provider(name: str, config: dict):
    if name not in PROVIDER_REGISTRY:
        raise ValueError(f"Provider {name} not registered")
    return PROVIDER_REGISTRY[name](config)
