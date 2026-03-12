#!/usr/bin/env python3
"""
ha-automation-studio CLI
AI toolkit for generating, analyzing and improving Home Assistant automations.
"""

import os
import sys
import click
from dotenv import load_dotenv
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel

load_dotenv()

console = Console()


def check_api_key():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        console.print(
            "[red]Error:[/red] ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
        )
        sys.exit(1)


@click.group()
@click.version_option("0.1.0")
def cli():
    """
    🏠 ha-automation-studio — AI toolkit for Home Assistant automations.

    Generate, analyze and optimize your automations using AI.
    """
    pass


@cli.command()
@click.argument("request")
@click.option("--model", default=None, help="AI model to use (default: claude-3-5-haiku-20241022)")
@click.option("--output", "-o", default=None, help="Save output to file")
def generate(request, model, output):
    """Generate a Home Assistant automation YAML from a natural language request.

    Example:

        python cli.py generate "turn on bedroom light when motion after sunset"
    """
    check_api_key()

    from ha_automation_studio.generator import generate_automation

    console.print(f"\n[bold blue]🤖 Generating automation for:[/bold blue] {request}\n")

    with console.status("[yellow]Calling AI...[/yellow]"):
        result = generate_automation(request, model=model)

    syntax = Syntax(result, "yaml", theme="monokai", line_numbers=True)
    console.print(Panel(syntax, title="[green]Generated Automation[/green]", border_style="green"))

    if output:
        with open(output, "w") as f:
            f.write(result)
        console.print(f"\n[green]✓ Saved to {output}[/green]")


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--model", default=None, help="AI model to use")
def analyze(file, model):
    """Analyze an existing Home Assistant automation YAML file.

    Example:

        python cli.py analyze examples/automations.yaml
    """
    check_api_key()

    from ha_automation_studio.analyzer import analyze_file

    console.print(f"\n[bold blue]🔍 Analyzing:[/bold blue] {file}\n")

    with console.status("[yellow]Analyzing automation...[/yellow]"):
        result = analyze_file(file, model=model)

    console.print(Panel(result, title="[yellow]Analysis Result[/yellow]", border_style="yellow"))


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--model", default=None, help="AI model to use")
@click.option("--output", "-o", default=None, help="Save optimized YAML to file")
def optimize(file, model, output):
    """Optimize an existing Home Assistant automation YAML file.

    Example:

        python cli.py optimize examples/automations.yaml
    """
    check_api_key()

    from ha_automation_studio.optimizer import optimize_file

    console.print(f"\n[bold blue]⚡ Optimizing:[/bold blue] {file}\n")

    with console.status("[yellow]Optimizing automation...[/yellow]"):
        result = optimize_file(file, model=model)

    console.print(Panel(result, title="[cyan]Optimization Result[/cyan]", border_style="cyan"))

    if output:
        with open(output, "w") as f:
            f.write(result)
        console.print(f"\n[green]✓ Saved to {output}[/green]")


if __name__ == "__main__":
    cli()
