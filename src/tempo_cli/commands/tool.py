from typing import Callable
from importlib.metadata import entry_points

import rich_click as click

from tempo_core import main_logic
from tempo_core.manager import tools_cache
from tempo_binary_tool_manager import manager


def load_external_tools() -> list[manager.ToolInfo]:
    eps = entry_points(group="tempo.tools")
    tools = []
    for ep in eps:
        tool_cls = ep.load()
        tool = tool_cls(cache=tools_cache)
        tools.append(tool)
    return tools


# ---- TOOL GROUP ----
@click.group()
def tool() -> None:
    """Tool related commands"""

  # attach tool group to main CLI


# ---- INSTALL GROUP ----
@click.group()
def install() -> None:
    """Install programs"""


  # attach install group under tool


# ---- UNINSTALL GROUP (example) ----
# @click.group()
# def uninstall():
#     """Uninstall programs"""


# tool.add_command(uninstall)  # attach uninstall group under tool


# ---- INSTALL COMMANDS ----

inited_tools = []
# for entry in manager.ToolInfo.registry:
#     if issubclass(entry, manager.ToolInfo):
#         entry = entry(cache=tools_cache)
#         inited_tools.append(entry)

inited_tools.extend(load_external_tools())

tools = [
    (
        entry.tool_name,
        f"Install {entry.tool_name[0].upper()}{entry.tool_name[1:].lower()}",
        entry.ensure_tool_installed,
    )
    for entry in inited_tools
]

def make_command(name: str, help_text: str, func: Callable) -> Callable:
    @install.command(name=name, help=help_text, short_help=help_text)
    @click.option(
        "--run_after_install",
        is_flag=True,
        default=False,
        type=bool,
        help="Should the installed program be run after installation.",
    )
    def _command(run_after_install: bool) -> None:
        func()


    return _command


for name, help_text, func in tools:
    make_command(name, help_text, func)
