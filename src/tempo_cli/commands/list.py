from tempo_cli.commands.tool import install
from pathlib import Path

import rich_click as click
from tempo_core import logger, registry


@click.group()
def list() -> None: # noqa
    """List related commands"""


command_help_list_unreal_installs = "List all detected unreal engine installs."


@list.command(
    name="unreal_installs",
    help=command_help_list_unreal_installs,
    short_help=command_help_list_unreal_installs,
)
def unreal_installs() -> None:
    unreal_installs = registry.get_unreal_installs_from_registry()
    if unreal_installs:
        for version, path in unreal_installs.items():
            logger.log_message(f"{version}: {path}")
    else:
        logger.log_message('There were no detected unreal engine installs.')


command_help_list_mods = "List all detected mod entries for the project."

@list.command(
    name="mods", help=command_help_list_mods, short_help=command_help_list_mods,
)
# have it take in the settings json
def mods() -> None:
    logger.log_message(f"message")


command_help_list_tools = "List all detected cached tools."

@list.command(
    name="tools", help=command_help_list_tools, short_help=command_help_list_tools,
)
def tools() -> None:
    logger.log_message(f"message")


command_help_list_uplugins = "List all detected uplugins used by the uproject."

@list.command(
    name="uplugins", help=command_help_list_uplugins, short_help=command_help_list_uplugins,
)
# have it take in the settings json
def uplugins() -> None:
    logger.log_message(f"message")

# clean param for the detection of unreal installs
# this would remove registry entries to places without actual installs that used to have them
