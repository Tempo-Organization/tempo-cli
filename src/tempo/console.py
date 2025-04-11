from rich.console import Console
from typing import Literal
import sys


def get_color_system_type() -> (
    Literal["auto", "standard", "256", "truecolor", "windows"] | None
):
    if "--rich_console_color_system" in sys.argv:
        index = sys.argv.index("--rich_console_color_system") + 1
        if index < len(sys.argv):
            value = sys.argv[index]
            if value == "none":
                return None
            if value in ("auto", "standard", "256", "truecolor", "windows"):
                return value
    return "auto"


def get_use_auto_console_highlight() -> bool:
    return True


console = Console(
    color_system=get_color_system_type(), highlight=get_use_auto_console_highlight()
)
