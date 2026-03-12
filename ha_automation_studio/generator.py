"""
Automation generator — converts natural language to Home Assistant YAML.
"""

import os
import anthropic
from .prompts import GENERATION_SYSTEM_PROMPT, GENERATION_USER_PROMPT


def generate_automation(user_request: str, model: str = None) -> str:
    """
    Generate Home Assistant automation YAML from a natural language request.

    Args:
        user_request: Natural language description of the desired automation.
        model: Claude model to use. Defaults to env var AI_MODEL or claude-3-5-haiku-20241022.

    Returns:
        Generated YAML string.
    """
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    model = model or os.environ.get("AI_MODEL", "claude-3-5-haiku-20241022")

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        system=GENERATION_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": GENERATION_USER_PROMPT.format(user_request=user_request),
            }
        ],
    )

    return message.content[0].text.strip()
