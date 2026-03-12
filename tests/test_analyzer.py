"""
Tests for ha-automation-studio analyzer.
"""

import pytest
from ha_automation_studio.analyzer import validate_yaml_structure

VALID_AUTOMATION = """
alias: Test automation
trigger:
  - platform: state
    entity_id: binary_sensor.motion
    to: "on"
action:
  - service: light.turn_on
    target:
      entity_id: light.test
mode: single
"""

MISSING_TRIGGER = """
alias: Missing trigger
action:
  - service: light.turn_on
    target:
      entity_id: light.test
mode: single
"""

MISSING_ACTION = """
alias: Missing action
trigger:
  - platform: state
    entity_id: binary_sensor.motion
    to: "on"
mode: single
"""

INVALID_YAML = """
alias: Bad YAML
  trigger: [unclosed
"""


def test_valid_automation_no_structural_issues():
    issues = validate_yaml_structure(VALID_AUTOMATION)
    assert len(issues) == 0


def test_missing_trigger_detected():
    issues = validate_yaml_structure(MISSING_TRIGGER)
    assert any("trigger" in i.lower() for i in issues)


def test_missing_action_detected():
    issues = validate_yaml_structure(MISSING_ACTION)
    assert any("action" in i.lower() for i in issues)


def test_invalid_yaml_detected():
    issues = validate_yaml_structure(INVALID_YAML)
    assert any("yaml" in i.lower() for i in issues)
