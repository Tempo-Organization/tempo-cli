import os
import pathlib

import rich_click as click
from tempo_core import main_logic, file_io, data_structures, settings
from tempo_core.programs import kismet_analyzer as tempo_core_kismet_analyzer


default_output_releases_dir = os.path.normpath(os.path.join(file_io.SCRIPT_DIR, "dist"))
default_releases_dir = os.path.normpath(
    os.path.join(
        str(settings.settings_information.settings_json_dir), "mod_packaging", "releases"
    )
)


@click.group()
def run():
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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def engine(settings_json):
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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def game(settings_json, toggle_engine):
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
        path_type=pathlib.Path,
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
        path_type=pathlib.Path,
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
        path_type=pathlib.Path,
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
        path_type=pathlib.Path,
    ),
    default=os.path.normpath(f'{os.getcwd()}/Modding/game_dump'),
    help="Path to an unpacked dir tree from an unreal game.",
)
@click.option(
    "--output",
    default=os.path.normpath(f'{os.getcwd()}/Modding/kismet_analyzer_dump'),
    type=click.Path(
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
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
def kismet_analyze_directory(settings_json, kismet_analyzer_executable, mappings, assets, output, open):
    if kismet_analyzer_executable:
        kismet_analyzer_directory = os.path.normpath(os.path.dirname(kismet_analyzer_executable))
    else:
        kismet_analyzer_directory = os.path.normpath(f'{os.getcwd()}/Modding/tools/kismet_analyzer')
    os.makedirs(output, exist_ok=True)
    if len(file_io.get_files_in_tree(assets)) < 1:
        raise RuntimeError('When kismet analyzing a directory, the provided assets path must not be an empty directory tree.')
    if tempo_core_kismet_analyzer.does_kismet_analyzer_exist(tempo_core_kismet_analyzer.get_kismet_analyzer_path(kismet_analyzer_directory)):
        tempo_core_kismet_analyzer.install_kismet_analyzer(kismet_analyzer_directory)
    tempo_core_kismet_analyzer.run_gen_cfg_tree_command(
        kismet_analyzer_executable=pathlib.Path(tempo_core_kismet_analyzer.get_kismet_analyzer_path(kismet_analyzer_directory)),
        mappings_file=mappings,
        asset_tree=assets,
        output_tree=output
    )
    if open:
        import webbrowser
        # check the below path is actually correct later on
        webbrowser.open(os.path.normpath(f'{output}/index.html'))


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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def test_mods(settings_json, mod_names, toggle_engine, use_symlinks):
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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def test_mods_all(settings_json, toggle_engine, use_symlinks):
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
    default=default_releases_dir,
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
)
@click.option(
    "--output_directory",
    default=default_output_releases_dir,
    help="Path to the output directory",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def full_run(
    settings_json,
    mod_names,
    toggle_engine,
    base_files_directory,
    output_directory,
    use_symlinks,
):
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
    default=default_releases_dir,
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
)
@click.option(
    "--output_directory",
    default=default_output_releases_dir,
    help="Path to the output directory",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
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
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def full_run_all(
    settings_json, toggle_engine, base_files_directory, output_directory, use_symlinks
):
    main_logic.full_run_all(
        toggle_engine=toggle_engine,
        base_files_directory=base_files_directory,
        output_directory=output_directory,
        use_symlinks=use_symlinks,
    )











host_type_choices = data_structures.get_enum_strings_from_enum(
    data_structures.UnrealHostTypes
)
loading_phase_choices = data_structures.get_enum_strings_from_enum(
    data_structures.LoadingPhases
)

command_help = "Adds the specified module entry to the descriptor file, overwriting if it already exists."


@run.command(
    name="add_module_to_descriptor", help=command_help, short_help=command_help
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
        path_type=pathlib.Path,
    ),
)
@click.argument("module_name", type=str)
def add_module_to_descriptor(descriptor_file, module_name, host_type, loading_phase):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the module to.
        module_name (str): Name of the module to add.
    """
    main_logic.add_module_to_descriptor(
        descriptor_file, module_name, host_type, loading_phase
    )


command_help = "Adds the specified plugin entry to the descriptor file, overwriting if it already exists."


@run.command(
    name="add_plugin_to_descriptor", help=command_help, short_help=command_help
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
        path_type=pathlib.Path,
    ),
)
@click.argument("plugin_name", type=str)
def add_plugin_to_descriptor(descriptor_file, plugin_name, is_enabled):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the plugin to.
        plugin_name (str): Name of the plugin to add.
    """
    main_logic.add_plugin_to_descriptor(
        descriptor_file, plugin_name, is_enabled=is_enabled
    )


command_help = (
    "Removes the module name entries in the provided descriptor file if they exist."
)


@run.command(
    name="remove_modules_from_descriptor", help=command_help, short_help=command_help
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
        path_type=pathlib.Path,
    ),
)
def remove_modules_from_descriptor(descriptor_file, module_names):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the modules from.
    """
    main_logic.remove_modules_from_descriptor(descriptor_file, module_names)


command_help = (
    "Removes the plugin name entries in the provided descriptor file if they exist."
)


@run.command(
    name="remove_plugins_from_descriptor", help=command_help, short_help=command_help
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
        path_type=pathlib.Path,
    ),
)
def remove_plugins_from_descriptor(descriptor_file, plugin_names):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the plugins from.
    """
    main_logic.remove_plugins_from_descriptor(descriptor_file, plugin_names)
