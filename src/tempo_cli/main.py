
import click
from click.termui import _build_prompt as _original_build_prompt

from tempo_cli import cli


def _style_prompt(prompt: str) -> str:
    return click.style(prompt, fg="magenta", bg="bright_white", bold=True)

def styled_build_prompt(
    text, prompt_suffix, show_default, default, show_choices, type_
):
    prompt = _original_build_prompt(
        text, prompt_suffix, show_default, default, show_choices, type_
    )
    return _style_prompt(prompt)


click.termui._build_prompt = styled_build_prompt


def main():
    cli.cli(windows_expand_args=False)
