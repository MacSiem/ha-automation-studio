"""
Automation optimizer — suggests and applies improvements to Home Assistant YAML automations.
"""

import os
import anthropic
from .prompts import OPTIMIZATION_SYSTEM_PROMPT, OPTIMIZATION_USER_PROMPT
from .analyzer import load_yaml


def optimize_automation(yaml_content: str, model: str = None) -> str:
    """
    Suggest optimizations for a Home Assistant automation YAML.

    Args:
        yaml_content: Raw YAML string of the automation.
        model: Claude model to use.

    Returns:
        Optimized YAML with explanation of changes.
    """
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    model = model or os.environ.get("AI_MODEL", "claude-3-5-haiku-20241022")

    message = client.messages.create(
        model=model,
        max_tokens=1500,
        system=OPTIMIZATION_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": OPTIMIZATION_USER_PROMPT.format(yaml_content=yaml_content),
            }
        ],
    )

    return message.content[0].text.strip()


def optimize_file(path: str, model: str = None) -> str:
    """Load a YAML file and optimize it."""
    yaml_content = load_yaml(path)
    return optimize_automation(yaml_content, model=model)
