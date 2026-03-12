"""
Automation analyzer — detects issues in existing Home Assistant YAML automations.
"""

import os
import yaml
import anthropic
from .prompts import ANALYSIS_SYSTEM_PROMPT, ANALYSIS_USER_PROMPT


def load_yaml(path: str) -> str:
    """Load and return raw YAML content from a file."""
    with open(path, "r") as f:
        return f.read()


def validate_yaml_structure(yaml_content: str) -> list[str]:
    """
    Basic structural validation before sending to AI.
    Returns a list of structural issues found.
    """
    issues = []
    try:
        data = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        return [f"Invalid YAML syntax: {e}"]

    if not isinstance(data, dict):
        issues.append("Automation must be a YAML mapping (dict), not a list or scalar.")
        return issues

    if "trigger" not in data and "triggers" not in data:
        issues.append("Missing required field: trigger")
    if "action" not in data and "actions" not in data:
        issues.append("Missing required field: action")
    if "alias" not in data:
        issues.append("Missing recommended field: alias")
    if "mode" not in data:
        issues.append("Missing recommended field: mode (single/restart/queued/parallel)")

    return issues


def analyze_automation(yaml_content: str, model: str = None) -> str:
    """
    Analyze a Home Assistant automation YAML using AI.

    Args:
        yaml_content: Raw YAML string of the automation.
        model: Claude model to use.

    Returns:
        Analysis result as a string.
    """
    structural_issues = validate_yaml_structure(yaml_content)

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    model = model or os.environ.get("AI_MODEL", "claude-3-5-haiku-20241022")

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        system=ANALYSIS_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": ANALYSIS_USER_PROMPT.format(yaml_content=yaml_content),
            }
        ],
    )

    ai_analysis = message.content[0].text.strip()

    if structural_issues:
        header = "## Structural Issues Found\n" + "\n".join(f"- {i}" for i in structural_issues)
        return f"{header}\n\n## AI Analysis\n{ai_analysis}"

    return ai_analysis


def analyze_file(path: str, model: str = None) -> str:
    """Load a YAML file and analyze it."""
    yaml_content = load_yaml(path)
    return analyze_automation(yaml_content, model=model)
