# Claude for Open Source — Application Description

> This file contains the project description prepared for the Anthropic Claude for Open Source program application.
> Program page: https://claude.com/contact-sales/claude-for-oss

---

## Project name

ha-automation-studio

## One-line description

Open-source AI CLI toolkit that generates, analyzes and optimizes Home Assistant automation YAML from natural language.

## Project description

ha-automation-studio is an open-source developer tool for the Home Assistant ecosystem. It uses Claude AI models to help Home Assistant users create, debug and improve their automation configurations.

Home Assistant has over 750,000 active installations worldwide. Automations are its most powerful feature — and also the most difficult to use correctly. YAML syntax, trigger/condition/action logic, and debugging complex automations are common pain points for both new and experienced users.

ha-automation-studio addresses this with three core capabilities:

**1. Automation generation**
Users describe what they want in plain English. The tool generates valid, ready-to-use Home Assistant YAML with correct trigger, condition, action and mode fields.

**2. Automation analysis**
The tool analyzes existing automation files and identifies structural errors, missing fields, logic problems and anti-patterns — both via local structural validation and AI-powered deep analysis.

**3. Automation optimization**
The tool suggests concrete improvements to existing automations: debounce logic, better trigger patterns, correct mode selection, simplified condition logic.

## How the project uses Claude

Claude models power all three core features:

- **Generation**: Claude converts natural language descriptions into valid Home Assistant YAML, using a carefully crafted system prompt that encodes Home Assistant best practices and syntax rules.
- **Analysis**: Claude performs deep logic analysis of existing automations — detecting issues that go beyond simple structural validation, such as triggers that may fire unexpectedly or missing conditions.
- **Optimization**: Claude suggests concrete improvements with explanations, acting as an experienced Home Assistant developer reviewing the automation.

All AI behavior is controlled through prompt templates in `prompts.py`, making it easy to iterate and improve without changing business logic.

## Why this project benefits from Claude for Open Source

The project is an open-source developer tool with no commercial model. All improvements go back to the Home Assistant community.

Access to Claude models through the program would allow:
- Using more capable models for complex automation analysis
- Running experiments with different prompting strategies to improve YAML quality
- Building more sophisticated features (automation reasoning, multi-file analysis) that require higher token limits
- Keeping the tool free for the community without usage costs limiting development

## Target audience

- Home Assistant users who want to create automations faster
- Smart home developers building automation tooling
- Home Assistant power users managing large automation collections
- AI developer tooling creators interested in home automation use cases

## Open source details

- License: MIT
- Repository: github.com/MacSiem/ha-automation-studio
- Contributions welcome from the Home Assistant community

## Roadmap highlights

- Phase 2: Home Assistant API integration for live entity discovery
- Phase 3: Home Assistant Add-on and REST API
- Phase 4: Frigate camera event analysis, ESPHome config generation

## Links

- GitHub: https://github.com/MacSiem/ha-automation-studio
- Home Assistant: https://www.home-assistant.io/
- Claude for Open Source: https://claude.com/contact-sales/claude-for-oss
