# Architecture

## Overview

ha-automation-studio is built as a modular Python toolkit with a clean separation between the CLI layer, the business logic, and the AI prompt layer.

```
┌─────────────────────────────────────────────────────┐
│                     cli.py                          │
│         (Click CLI — generate / analyze / optimize) │
└──────────┬──────────────┬──────────────┬────────────┘
           │              │              │
    ┌──────▼──────┐ ┌─────▼──────┐ ┌───▼────────┐
    │ generator.py│ │analyzer.py │ │optimizer.py│
    │             │ │            │ │            │
    │ NL → YAML   │ │ Validation │ │ Suggestions│
    │             │ │ + AI audit │ │            │
    └──────┬──────┘ └─────┬──────┘ └───┬────────┘
           │              │              │
           └──────────────▼──────────────┘
                    ┌────────────┐
                    │ prompts.py │
                    │            │
                    │  All AI    │
                    │  templates │
                    └─────┬──────┘
                          │
                    ┌─────▼──────┐
                    │ Anthropic  │
                    │ Claude API │
                    └────────────┘
```

## Modules

### `cli.py`
Entry point. Uses [Click](https://click.palletsprojects.com/) for command parsing and [Rich](https://github.com/Textualize/rich) for terminal output. No business logic — delegates entirely to the core modules.

### `ha_automation_studio/generator.py`
Converts natural language descriptions into Home Assistant automation YAML. Calls Claude with a structured system prompt and returns the raw YAML string.

### `ha_automation_studio/analyzer.py`
Two-stage analysis:
1. **Structural validation** (no API call) — checks for missing `trigger`, `action`, `alias`, `mode` fields using `pyyaml`
2. **AI analysis** — sends automation to Claude for deeper logic analysis, pattern detection and improvement suggestions

### `ha_automation_studio/optimizer.py`
Sends an existing automation to Claude with an optimization-focused prompt. Returns improved YAML with a diff-style explanation of each change.

### `ha_automation_studio/prompts.py`
All AI prompt templates in one place. Separating prompts from code makes it easy to:
- Tune AI behavior without touching business logic
- Add support for different AI providers
- A/B test prompt variations

## Design principles

**Prompt-driven behavior** — AI behavior is controlled entirely through prompt templates. Improving the tool often means improving a prompt, not changing Python code.

**Two-layer validation** — structural checks run locally (fast, free, no API needed), AI analysis runs on top for deeper issues.

**Provider-agnostic structure** — the generator, analyzer and optimizer accept a `model` parameter. Adding OpenAI or Ollama support means adding a new client in each module without changing the CLI or prompt layer.

**Single file CLI** — `cli.py` is self-contained. Users can run it directly without understanding the package internals.

## Adding a new AI provider

1. Add provider client import in the relevant module (e.g. `generator.py`)
2. Read `AI_PROVIDER` from env (e.g. `anthropic`, `openai`, `ollama`)
3. Route to the appropriate client while reusing the same prompt templates from `prompts.py`

## Future architecture (Phase 3+)

```
ha-automation-studio/
├── ha_automation_studio/
│   ├── core/               # Current modules (generator, analyzer, optimizer)
│   ├── api/                # FastAPI REST API layer
│   ├── addon/              # Home Assistant Add-on wrapper
│   ├── providers/          # AI provider adapters (Claude, OpenAI, Ollama)
│   └── ha_client/          # Home Assistant REST API client (entity discovery)
```
