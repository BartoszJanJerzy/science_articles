import yaml
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    openai_chat_model: str
    gemini_chat_model: str
    ai_provider: str


config = Config(**yaml.safe_load(open(os.path.join("resources", "config.yaml"))))
