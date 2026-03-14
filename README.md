<div align="center">

# ð  Home Assistant Automation Studio

**AI toolkit for generating, analyzing and improving Home Assistant automations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-compatible-41BDF5.svg)](https://www.home-assistant.io/)
[![Powered by Claude](https://img.shields.io/badge/AI-Claude%20by%20Anthropic-orange.svg)](https://www.anthropic.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

*Stop writing YAML by hand. Describe what you want, get a working automation.*

[Quick Start](#-quick-start) Â· [Features](#-features) Â· [Examples](#-examples) Â· [Roadmap](#ï¸-roadmap) Â· [Contributing](#-contributing)

</div>

---

## The problem

Home Assistant automations are powerful â but YAML is painful.

New users spend hours on syntax errors. Experienced users maintain hundreds of automations with no tooling. Everyone debugs automation logic by trial and error.

**ha-automation-studio fixes that with AI.**

---

## â¨ Features

| Feature | Description |
|---|---|
| ð¤ **Generate** | Natural language â valid HA YAML in seconds |
| ð **Analyze** | Detect missing fields, logic errors, bad patterns |
| â¡ **Optimize** | Debounce, modes, trigger improvements suggested automatically |
| ð¥ï¸ **CLI** | Works in terminal, scripts, CI pipelines |

---

## ð¦ Quick Start

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

## ð¡ Examples

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
â  WARNING  Missing debounce on binary_sensor.motion â may trigger repeatedly
â  WARNING  No mode set â defaults to single, consider restart for motion lights
â¹ INFO     Condition block could use time_pattern trigger instead
â No critical issues found
```

### Optimize and apply improvements

```bash
python cli.py optimize my_automations.yaml --output improved.yaml
```

---

## ð Project Structure

```
ha-automation-studio/
âââ cli.py                          # Entry point â generate / analyze / optimize
âââ ha_automation_studio/
â   âââ generator.py                # Natural language â YAML
â   âââ analyzer.py                 # Structural validation + AI analysis
â   âââ optimizer.py                # Improvement suggestions
â   âââ prompts.py                  # AI prompt templates (easy to customize)
âââ examples/
â   âââ automations.yaml            # Ready to test examples
âââ tests/                          # pytest test suite
âââ docs/
    âââ ARCHITECTURE.md
    âââ CONTRIBUTING.md
```

---

## ðºï¸ Roadmap

**Phase 1 â MVP CLI** *(current)*
- [x] `generate` command
- [x] `analyze` command with structural validation
- [x] `optimize` command
- [ ] `--stdin` support for pipe workflows

**Phase 2 â Developer Tools**
- [ ] Home Assistant API integration (live entity discovery)
- [ ] Automation debugging mode
- [ ] OpenAI + local LLM support (Ollama)
- [ ] `--watch` mode for auto-analysis on file save

**Phase 3 â Home Assistant Integration**
- [ ] Home Assistant Add-on
- [ ] REST API
- [ ] Web UI

**Phase 4 â AI Agents**
- [ ] Automation reasoning engine
- [ ] Frigate camera event analysis
- [ ] ESPHome configuration generation
- [ ] Smart energy automation suggestions

---

## ð¤ Contributing

Contributions are very welcome. See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

**Good first issues:**
- Add `--stdin` support to CLI
- Improve YAML analysis prompt
- Add more example automations
- Write additional tests

---

## ð License

MIT â see [LICENSE](LICENSE).

---

## ð Acknowledgements

- [Home Assistant](https://www.home-assistant.io/) â the best open source home automation platform
- [Anthropic Claude](https://www.anthropic.com/) â AI models powering this toolkit
- The Home Assistant community for inspiration and feedback

---

## Support

If you find this project useful, consider supporting its development:

<a href="https://buymeacoffee.com/macsiem" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50" ></a>
<a href="https://www.paypal.com/donate/?hosted_button_id=Y967H4PLRBN8W" target="_blank"><img src="https://img.shields.io/badge/PayPal-Donate-blue?logo=paypal&logoColor=white" alt="PayPal Donate" height="50" ></a>
