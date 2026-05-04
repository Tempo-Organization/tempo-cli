import os
from pathlib import Path

import rich_click as click
from ue4ss_installer_core import ue4ss

from tempo_core import main_logic, file_io, data_structures, settings, manager
from tempo_core.programs import kismet_analyzer as tempo_core_kismet_analyzer

from tempo_binary_tools import kismet_analyzer as kismet_analyzer_tool


# make this only happen if online is working, if online not working, throw error when calling related commands
# ue4ss.cache_repo_releases_info("UE4SS-RE", "RE-UE4SS")


@click.group()
def run() -> None:
    """Run related commands"""


command_help = "Run the engine."

@run.command(name="engine", help=command_help, short_help=command_help)
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
def engine(settings_json: Path) -> None:
    main_logic.run_engine()


command_help = "Run the game."

@run.command(name="game", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    default=False,
    type=bool,
    help="Whether to close engine instances at the start and open at the end of the command process (default: False).",
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
def game(settings_json: Path, toggle_engine: bool) -> None:
    main_logic.run_game(toggle_engine=toggle_engine)


@run.command(
    name="kismet_analyze_directory",
    help="Generates a kismet analyzer dump for the provided directory tree.",
    short_help="Generates a kismet analyzer dump for the provided directory tree.",
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
@click.option(
    "--kismet_analyzer_executable",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=False,
    help="Path to your kismet analyzer executable, if not provided, one will be automatically downloaded.",
)
@click.option(
    "--mappings",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=False,
    help="Path to a jmap or usmap file.",
)
@click.option(
    "--assets",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    default=Path(f'{Path.cwd()}/Modding/game_dump'),
    help="Path to an unpacked dir tree from an unreal game.",
)
@click.option(
    "--output",
    default=Path(f'{Path.cwd()}/Modding/kismet_analyzer_dump'),
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    help="The file location you want your utoc outputted to.",
)
@click.option(
    "--open",
    is_flag=True,
    default=False,
    type=bool,
    help="Should the generated kismet analyzer be opened after being completed.",
)
def kismet_analyze_directory(mappings: Path, assets: Path, output: Path, open: bool) -> None: # noqa
    output.mkdir(parents=True, exist_ok=True)
    if len(file_io.get_files_in_tree(assets)) < 1:
        raise RuntimeError('When kismet analyzing a directory, the provided assets path must not be an empty directory tree.')
    tempo_core_kismet_analyzer.run_gen_cfg_tree_command(
        kismet_analyzer_executable=Path(kismet_analyzer_tool.KismetAnalyzerToolInfo(cache=manager.tools_cache).get_executable_path()),
        mappings_file=mappings,
        asset_tree=assets,
        output_tree=output,
    )
    if open:
        import webbrowser
        # check the below path is actually correct later on
        webbrowser.open(str(Path(output / 'index.html')))


command_help = "Run tests for specific mods"


@run.command(name="test_mods", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="A mod name, can be specified multiple times",
)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to close engine instances at the start and open at the end of the command process",
)
@click.option(
    "--use_symlinks",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to use symlinks to save time with file operations",
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
def test_mods(settings_json: Path, mod_names: list[str], toggle_engine: bool, use_symlinks: bool) -> None:
    main_logic.test_mods(
        input_mod_names=mod_names,
        toggle_engine=toggle_engine,
        use_symlinks=use_symlinks,
    )


command_help = "Run tests for all mods within the specified settings JSON"


@run.command(name="test_mods_all", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to close engine instances at the start and open at the end of the command process",
)
@click.option(
    "--use_symlinks",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to use symlinks to save time with file operations",
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
def test_mods_all(settings_json: Path, toggle_engine: bool, use_symlinks: bool) -> None:
    main_logic.test_mods_all(toggle_engine=toggle_engine, use_symlinks=use_symlinks)


command_help = "Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for the specified mod names."


@run.command(name="full_run", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="A mod name, can be specified multiple times",
)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Will close engine instances at the start and open at the end of the command process",
)
@click.option(
    "--base_files_directory",
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
)
@click.option(
    "--output_directory",
    help="Path to the output directory",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
)
@click.option(
    "--use_symlinks",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to use symlinks to save time with file operations",
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
def full_run(
    settings_json: Path,
    mod_names: list[str],
    toggle_engine: bool,
    base_files_directory: Path,
    output_directory: Path,
    use_symlinks: bool,
) -> None:
    if not base_files_directory or base_files_directory == '':
        base_files_directory = Path(settings.get_default_release_base_files_dir())
    if not output_directory or output_directory == '':
        output_directory = Path(settings.get_default_release_dir())
    main_logic.full_run(
        input_mod_names=mod_names,
        toggle_engine=toggle_engine,
        base_files_directory=base_files_directory,
        output_directory=output_directory,
        use_symlinks=use_symlinks,
    )


command_help = "Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for all mod entries within the specified settings JSON."


@run.command(name="full_run_all", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Will close engine instances at the start and open at the end of the command process",
)
@click.option(
    "--base_files_directory",
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
)
@click.option(
    "--output_directory",
    help="Path to the output directory",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
)
@click.option(
    "--use_symlinks",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to use symlinks to save time with file operations",
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
def full_run_all(
    settings_json: Path, toggle_engine: bool, base_files_directory: Path, output_directory: Path, use_symlinks: bool,
) -> None:
    if not base_files_directory or base_files_directory == '':
        base_files_directory = Path(settings.get_default_release_base_files_dir())
    if not output_directory or output_directory == '':
        output_directory = Path(settings.get_default_release_dir())
    main_logic.full_run_all(
        toggle_engine=toggle_engine,
        base_files_directory=base_files_directory,
        output_directory=output_directory,
        use_symlinks=use_symlinks,
    )











host_type_choices = data_structures.get_enum_strings_from_enum(
    data_structures.UnrealHostTypes,
)
loading_phase_choices = data_structures.get_enum_strings_from_enum(
    data_structures.LoadingPhases,
)

command_help = "Adds the specified module entry to the descriptor file, overwriting if it already exists."


@run.command(
    name="add_module_to_descriptor", help=command_help, short_help=command_help,
)
@click.option(
    "--host_type",
    type=click.Choice(host_type_choices),
    default=data_structures.UnrealHostTypes.DEVELOPER.value,
    required=True,
    help="The host type to use.",
)
@click.option(
    "--loading_phase",
    type=click.Choice(loading_phase_choices),
    default=data_structures.LoadingPhases.DEFAULT.value,
    required=True,
    help="The loading phase to use.",
)
@click.argument(
    "descriptor_file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.argument("module_name", type=str)
def add_module_to_descriptor(descriptor_file: Path, module_name: str, host_type: str, loading_phase: str) -> None:
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the module to.
        module_name (str): Name of the module to add.
    """
    main_logic.add_module_to_descriptor(
        descriptor_file, module_name, host_type, loading_phase,
    )


command_help = "Adds the specified plugin entry to the descriptor file, overwriting if it already exists."


@run.command(
    name="add_plugin_to_descriptor", help=command_help, short_help=command_help,
)
@click.option(
    "--is_enabled",
    default=True,
    type=bool,
    help="Whether or not Enabled is ticked for the plugin entry.",
)
@click.argument(
    "descriptor_file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
@click.argument("plugin_name", type=str)
def add_plugin_to_descriptor(descriptor_file: Path, plugin_name: str, is_enabled: bool) -> None:
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the plugin to.
        plugin_name (str): Name of the plugin to add.
    """
    main_logic.add_plugin_to_descriptor(
        descriptor_file, plugin_name, is_enabled=is_enabled,
    )


command_help = (
    "Removes the module name entries in the provided descriptor file if they exist."
)


@run.command(
    name="remove_modules_from_descriptor", help=command_help, short_help=command_help,
)
@click.option(
    "--module_names",
    multiple=True,
    type=str,
    required=True,
    help="A module name to remove from the descriptor file, can be specified multiple times.",
)
@click.argument(
    "descriptor_file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
def remove_modules_from_descriptor(descriptor_file: Path, module_names: list[str]) -> None:
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the modules from.
    """
    main_logic.remove_modules_from_descriptor(descriptor_file, module_names)


command_help = (
    "Removes the plugin name entries in the provided descriptor file if they exist."
)


@run.command(
    name="remove_plugins_from_descriptor", help=command_help, short_help=command_help,
)
@click.option(
    "--plugin_names",
    multiple=True,
    type=str,
    required=True,
    help="A plugin name to remove from the descriptor file, can be specified multiple times.",
)
@click.argument(
    "descriptor_file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
)
def remove_plugins_from_descriptor(descriptor_file: Path, plugin_names: list[str]) -> None:
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the plugins from.
    """
    main_logic.remove_plugins_from_descriptor(descriptor_file, plugin_names)


@run.command(
    name="install_ue4ss", help=command_help, short_help=command_help,
)
@click.option(
    "--release_tag",
    type=str,
    default=ue4ss.get_default_ue4ss_version_tag(),
    help="The release tag of the ue4ss release you want to install. Defaults to the latest release.",
)
@click.option(
    "--game_exe_directory",
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    help="The directory containing the main executable for your game. Defaults to the dir that contains the game exe specified within the tempo config.",
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
    required=False,
    help="Path to the settings JSON file",
)
def install_ue4ss(release_tag: str, game_exe_directory: Path, settings_json: Path) -> None:
    cache_dir = Path(f'{manager.tools_cache.get_download_dir()}/lazy_cache/ue4ss/{release_tag}')
    cache_dir.mkdir(parents=True, exist_ok=True)
    ue4ss.install_ue4ss_to_dir(
        str(cache_dir),
        str(game_exe_directory),
        release_tag,
    )
