import click
from click.termui import _build_prompt as _original_build_prompt
from tempo_cli import cli
from rich.style import Style
from rich.text import Text

from tempo_core import log_info
from tempo_core.console import console


def _rich_build_prompt(prompt_text: str, fg=log_info.LOG_INFO['default_color'], bg=log_info.LOG_INFO['background_color']):
    style = Style(color=f"rgb{fg}", bgcolor=f"rgb{bg}")
    rich_text = Text(prompt_text, style=style)
    console.print(rich_text, end="")
    return ""


def styled_build_prompt(text, prompt_suffix, show_default, default, show_choices, type_):
    prompt = _original_build_prompt(
        text, prompt_suffix, show_default, default, show_choices, type_
    )
    _rich_build_prompt(prompt)
    return ""


click.termui._build_prompt = styled_build_prompt


def main():
    cli.cli(windows_expand_args=False)
