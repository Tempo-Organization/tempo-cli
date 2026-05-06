import json
from pathlib import Path

from tempo_cli.commands.tool import install

import rich_click as click
from tempo_core import logger, registry, settings, manager


@click.group()
def list() -> None: # noqa
    """List related commands"""


command_help_list_unreal_installs = "List all detected unreal engine installs."


@list.command(
    name="unreal_installs",
    help=command_help_list_unreal_installs,
    short_help=command_help_list_unreal_installs,
)
@click.option(
    "--clean",
    type=bool,
    is_flag=True,
    help="Will remove registry entries that don't actually contain unreal engine installs. May have to run with administrator permissions.",
)
def unreal_installs(clean: bool) -> None:
    unreal_installs = registry.get_unreal_installs_from_registry()
    if unreal_installs:
        for version, path in unreal_installs.items():
            logger.log_message(f"{version}: {path}")
    else:
        logger.log_message('There were no detected unreal engine installs.')
    if clean:
        registry.remove_invalid_unreal_engine_registry_entries()


command_help_list_mods = "List all detected mod entries for the project."

@list.command(
    name="mods", help=command_help_list_mods, short_help=command_help_list_mods,
)
@click.option(
    "--settings_json",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def mods(settings_json: Path) -> None:
    mods_dict = settings.get_mods_info_dict_from_json()
    for key, value in mods_dict.items():
        logger.log_message(key)
        logger.log_message(json.dumps(value, indent=4))


command_help_list_tools = "List all detected cached tools."

@list.command(
    name="tools", help=command_help_list_tools, short_help=command_help_list_tools,
)
def tools() -> None:
    manager.tools_cache.list_tools()


command_help_list_uplugins = "List all detected uplugins used by the uproject."

@list.command(
    name="uplugins", help=command_help_list_uplugins, short_help=command_help_list_uplugins,
)
@click.option(
    "--settings_json",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def uplugins(settings_json: Path) -> None:
    with settings_json.open("r", encoding="utf-8") as f:
        settings = json.load(f)

    try:
        uproject_path = settings["engine_info"]["unreal_project_file"]
    except KeyError:
        logger.log_message("Missing 'engine_info.unreal_project_file' in settings.")
        return

    uproject_path = (settings_json.parent / uproject_path).resolve()

    if not uproject_path.exists():
        logger.log_message(f"Uproject file not found: {uproject_path}")
        return

    with uproject_path.open("r", encoding="utf-8") as f:
        uproject = json.load(f)

    plugins = uproject.get("Plugins", [])

    if not plugins:
        logger.log_message("No plugins found.")
        return

    for plugin in plugins:
        name = plugin.get("Name", "Unknown")
        logger.log_message(f"Plugin: {name}")

        for key, value in plugin.items():
            if key != "Name":
                logger.log_message(f"  {key}: {value}")

        logger.log_message('')
