import yaml
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Prompts:
    instructions: str
    parse_response: str
    article_presentation: str


prompts = Prompts(**yaml.safe_load(open(os.path.join("resources", "prompts.yaml"))))
