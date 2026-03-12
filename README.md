<div align="center">

# 🏠 Home Assistant Automation Studio

**AI toolkit for generating, analyzing and improving Home Assistant automations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-compatible-41BDF5.svg)](https://www.home-assistant.io/)
[![Powered by Claude](https://img.shields.io/badge/AI-Claude%20by%20Anthropic-orange.svg)](https://www.anthropic.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

*Stop writing YAML by hand. Describe what you want, get a working automation.*

[Quick Start](#-quick-start) · [Features](#-features) · [Examples](#-examples) · [Roadmap](#️-roadmap) · [Contributing](#-contributing)

</div>

---

## The problem

Home Assistant automations are powerful — but YAML is painful.

New users spend hours on syntax errors. Experienced users maintain hundreds of automations with no tooling. Everyone debugs automation logic by trial and error.

**ha-automation-studio fixes that with AI.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **Generate** | Natural language → valid HA YAML in seconds |
| 🔍 **Analyze** | Detect missing fields, logic errors, bad patterns |
| ⚡ **Optimize** | Debounce, modes, trigger improvements suggested automatically |
| 🖥️ **CLI** | Works in terminal, scripts, CI pipelines |

---

## 📦 Quick Start

```bash
# 1. Clone and install
git clone https://github.com/MacSiem/ha-automation-studio
cd ha-automation-studio
pip install -r requirements.txt

# 2. Add your API key
cp .env.example .env
# Edit .env and add: ANTHROPIC_API_KEY=your_key_here

# 3. Generate your first automation
python cli.py generate "turn on bedroom light when motion after sunset"
```

---

## 💡 Examples

### Generate an automation from plain English

```bash
python cli.py generate "notify me when front door opens between 10pm and 6am"
```

```yaml
alias: Front door night alert
trigger:
  - platform: state
    entity_id: binary_sensor.front_door
    to: "on"
condition:
  - condition: time
    after: "22:00:00"
    before: "06:00:00"
action:
  - service: notify.mobile_app
    data:
      title: "Security Alert"
      message: "Front door opened at night"
mode: single
```

### Analyze an existing automation file

```bash
python cli.py analyze my_automations.yaml
```

```
⚠ WARNING  Missing debounce on binary_sensor.motion — may trigger repeatedly
⚠ WARNING  No mode set — defaults to single, consider restart for motion lights
ℹ INFO     Condition block could use time_pattern trigger instead
✓ No critical issues found
```

### Optimize and apply improvements

```bash
python cli.py optimize my_automations.yaml --output improved.yaml
```

---

## 📁 Project Structure

```
ha-automation-studio/
├── cli.py                          # Entry point — generate / analyze / optimize
├── ha_automation_studio/
│   ├── generator.py                # Natural language → YAML
│   ├── analyzer.py                 # Structural validation + AI analysis
│   ├── optimizer.py                # Improvement suggestions
│   └── prompts.py                  # AI prompt templates (easy to customize)
├── examples/
│   └── automations.yaml            # Ready to test examples
├── tests/                          # pytest test suite
└── docs/
    ├── ARCHITECTURE.md
    └── CONTRIBUTING.md
```

---

## 🗺️ Roadmap

**Phase 1 — MVP CLI** *(current)*
- [x] `generate` command
- [x] `analyze` command with structural validation
- [x] `optimize` command
- [ ] `--stdin` support for pipe workflows

**Phase 2 — Developer Tools**
- [ ] Home Assistant API integration (live entity discovery)
- [ ] Automation debugging mode
- [ ] OpenAI + local LLM support (Ollama)
- [ ] `--watch` mode for auto-analysis on file save

**Phase 3 — Home Assistant Integration**
- [ ] Home Assistant Add-on
- [ ] REST API
- [ ] Web UI

**Phase 4 — AI Agents**
- [ ] Automation reasoning engine
- [ ] Frigate camera event analysis
- [ ] ESPHome configuration generation
- [ ] Smart energy automation suggestions

---

## 🤝 Contributing

Contributions are very welcome. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

**Good first issues:**
- Add `--stdin` support to CLI
- Improve YAML analysis prompt
- Add more example automations
- Write additional tests

---

## 📄 License

MIT — see [LICENSE](LICENSE).

---

## 🔗 Acknowledgements

- [Home Assistant](https://www.home-assistant.io/) — the best open source home automation platform
- [Anthropic Claude](https://www.anthropic.com/) — AI models powering this toolkit
- The Home Assistant community for inspiration and feedback
