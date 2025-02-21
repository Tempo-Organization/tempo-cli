import os
import sys
import click
import pathlib
from trogon import tui

from unreal_auto_mod import (
    data_structures,
    main_logic,
    file_io,
    window_management,
    _version
)


default_releases_dir = os.path.normpath(os.path.join(main_logic.settings_json_dir, 'mod_packaging', 'releases'))
default_output_releases_dir = os.path.normpath(os.path.join(file_io.SCRIPT_DIR, 'dist'))
os.makedirs(default_releases_dir, exist_ok=True)
os.makedirs(default_output_releases_dir, exist_ok=True)

window_management.change_window_name('unreal_auto_mod')


def check_generate_wrapper():
    if "--generate_wrapper" in sys.argv:
        main_logic.generate_wrapper()


@tui()
@click.version_option(version=_version.version)
@click.group(chain=True)
@click.option('--generate_wrapper', is_flag=True, default=False, type=bool, help='Generate a wrapper that contains the current commandline.')
def cli(generate_wrapper, max_content_width=200):
    check_generate_wrapper()
    pass


command_help = 'Builds the uproject specified within the settings JSON'
@cli.command(name='build', help=command_help, short_help=command_help)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Will close engine instances at the start and open at the end of the command process')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def build(settings_json, toggle_engine):
    """
    Arguments:
        settings_json (string): Path to the settings JSON file
    """
    main_logic.build(settings_json, toggle_engine)


command_help = 'Cooks content for the uproject specified within the settings JSON'
@cli.command(name='cook', help=command_help, short_help=command_help)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Will close engine instances at the start and open at the end of the command process')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def cook(settings_json, toggle_engine):
    """
    Arguments:
        settings_json (string): Path to the settings JSON file
    """
    main_logic.cook(settings_json, toggle_engine)


command_help = 'Package content for the uproject specified within the settings JSON'
@cli.command(name='package', help=command_help, short_help=command_help)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Whether or not to close engine instances at the start and open at the end of the command process')
@click.option("--use_symlinks", is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def package(settings_json, toggle_engine, use_symlinks):
    """
    Arguments:
        settings_json (string): Path to the settings JSON file
    """
    main_logic.package(settings_json, toggle_engine, use_symlinks)


command_help = 'Run tests for specific mods'
@cli.command(name='test_mods', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='A mod name, can be specified multiple times')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Whether or not to close engine instances at the start and open at the end of the command process')
@click.option("--use_symlinks", is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def test_mods(settings_json, mod_names, toggle_engine, use_symlinks):
    """
    Arguments:
        settings_json (string): Path to the settings JSON file
    """
    main_logic.test_mods(settings_json, mod_names, toggle_engine, use_symlinks)


command_help = 'Run tests for all mods within the specified settings JSON'
@cli.command(name='test_mods_all', help=command_help, short_help=command_help)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Whether or not to close engine instances at the start and open at the end of the command process')
@click.option("--use_symlinks", is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def test_mods_all(settings_json, toggle_engine, use_symlinks):
    """
    Arguments:
        settings_json (string): Path to the settings JSON file
    """
    main_logic.test_mods_all(settings_json, toggle_engine, use_symlinks)


command_help = 'Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for the specified mod names.'
@cli.command(name='full_run', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='A mod name, can be specified multiple times')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Will close engine instances at the start and open at the end of the command process')
@click.option(
    "--base_files_directory", 
    default=default_releases_dir, 
    help='Path to dir tree whose content to pack alongside the mod for release', 
    type=click.Path(
        exists=False,
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option(
    "--output_directory", 
    default=default_output_releases_dir, 
    help='Path to the output directory', 
    type=click.Path(
        exists=False,
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def full_run_all(settings_json, mod_names, toggle_engine, base_files_directory, output_directory, use_symlinks):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file
    """
    main_logic.full_run(settings_json, mod_names, toggle_engine, base_files_directory, output_directory, use_symlinks)


command_help = 'Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for all mod entries within the specified settings JSON.'
@cli.command(name='full_run_all', help=command_help, short_help=command_help)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool, help='Will close engine instances at the start and open at the end of the command process')
@click.option(
    "--base_files_directory", 
    default=default_releases_dir, 
    help='Path to dir tree whose content to pack alongside the mod for release', 
    type=click.Path(
        exists=False,
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option(
    "--output_directory", 
    default=default_output_releases_dir, 
    help='Path to the output directory', 
    type=click.Path(
        exists=False,
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def full_run_all(settings_json, toggle_engine, base_files_directory, output_directory, use_symlinks):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file
    """
    main_logic.full_run_all(settings_json, toggle_engine, base_files_directory, output_directory, use_symlinks)


command_help = 'Generates mods for the specified mod names.'
@cli.command(name='generate_mods', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='A mod name, can be specified multiple times')
@click.option('--use_symlinks', is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_mods(settings_json, mod_names, use_symlinks):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file
    """
    main_logic.generate_mods(settings_json, mod_names, use_symlinks)


command_help = 'Generates mods for all enabled mods within the specified settings JSON.'
@cli.command(name='generate_mods_all', help=command_help, short_help=command_help)
@click.option('--use_symlinks', is_flag=True, default=False, type=bool, help='Whether or not to use symlinks to save time with file operations')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_mods_all(settings_json, use_symlinks):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file
    """
    main_logic.generate_mods_all(settings_json, use_symlinks)


command_help = 'Generate one or more mod releases.'
@cli.command(name='generate_mod_releases', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='A mod name, can be specified multiple times')
@click.option(
    "--base_files_directory", 
    default=default_releases_dir, 
    help='Path to dir tree whose content to pack alongside the mod for release', 
    type=click.Path(
        exists=True, 
        file_okay=False, 
        dir_okay=True, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option(
    "--output_directory", 
    default=default_output_releases_dir, 
    help='Path to the output directory', 
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True, path_type=pathlib.Path)
)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_mod_releases(settings_json, mod_names, base_files_directory, output_directory):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.generate_mod_releases(settings_json, mod_names, base_files_directory, output_directory)


command_help = 'Generate mod releases for all mods within the specified settings JSON.'
@cli.command(name='generate_mod_releases_all', help=command_help, short_help=command_help)
@click.option(
    "--base_files_directory", 
    default=default_releases_dir, 
    help='Path to dir tree whose content to pack alongside the mod for release', 
    type=click.Path(
        exists=True, 
        file_okay=False, 
        dir_okay=True, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option(
    "--output_directory", 
    default=default_output_releases_dir, 
    help='Path to the output directory', 
    type=click.Path(
        exists=True, 
        file_okay=False, 
        dir_okay=True, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_mod_releases_all(settings_json, base_files_directory, output_directory):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.generate_mod_releases_all(settings_json, base_files_directory, output_directory)


command_help = 'Cleans up the GitHub repository specified within the settings JSON.'
@cli.command(name='cleanup_full', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def cleanup_full(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_full(settings_json)


command_help = 'Cleans up the directories made from cooking of the GitHub repository specified within the settings JSON.'
@cli.command(name='cleanup_cooked', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def cleanup_cooked(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_cooked(settings_json)


command_help = 'Cleans up the directories made from building of the GitHub repository specified within the settings JSON.'
@cli.command(name='cleanup_build', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def cleanup_build(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_build(settings_json)


command_help = '''
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate a file list JSON, use the generate_file_list_json command.
'''
@cli.command(name='cleanup_game', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def cleanup_game(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_game(settings_json)


command_help = 'Generates a JSON file containing all of the files in the game directory, from the game exe specified within the settings JSON.'
@cli.command(name='generate_game_file_list_json', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_game_file_list_json(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.generate_game_file_list_json(settings_json)


command_help = '''
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate one, use the generate_file_list command.
'''
@cli.command(name='cleanup_from_file_list', help=command_help, short_help=command_help)
@click.argument('file_list', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True, path_type=pathlib.Path))
def cleanup_from_file_list(file_list, directory):
    """
    Arguments:
        file_list (str): Path to the file list you want to clean from.
        directory (str): Path to the directory tree to clean up. It will delete all files not in the specified file list.
    """
    main_logic.cleanup_from_file_list(file_list, directory)


command_help = 'Generates a JSON file containing all of the files in the specified directory.'
@cli.command(name='generate_file_list', help=command_help, short_help=command_help)
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True, path_type=pathlib.Path))
@click.argument('file_list', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def generate_file_list(directory, file_list):
    """
    Arguments:
        directory (str): Path to the directory tree you want to generate the file list from.
        file_list (str): Path to the output file, saved in JSON format.
    """
    main_logic.generate_file_list(directory, file_list)


command_help = 'Uploads the latest changes of the git project to the GitHub repository and branch specified within the settings JSON.'
@cli.command(name='upload_changes_to_repo', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def upload_changes_to_repo(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.upload_changes_to_repo(settings_json)


command_help = 'Cleans up and resyncs a git project to the GitHub repository and branch specified within the settings JSON.'
@cli.command(name='resync_dir_with_repo', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def resync_dir_with_repo(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.resync_dir_with_repo(settings_json)


command_help = 'Opens the latest log file.'
@cli.command(name='open_latest_log', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def open_latest_log(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.open_latest_log(settings_json)


command_help = 'Enable the given mod names in the provided settings JSON.'
@cli.command(name='enable_mods', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='Name of a mod to enable, can be specified multiple times')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def enable_mods(settings_json, mod_names):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.enable_mods(settings_json, mod_names)


command_help = 'Disable the given mod names in the provided settings JSON.'
@cli.command(name='disable_mods', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='Name of a mod to disable, can be specified multiple times')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def disable_mods(settings_json, mod_names):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.disable_mods(settings_json, mod_names)


command_help = 'Adds the given mod name in the provided settings JSON.'
@cli.command(name='add_mod', help=command_help, short_help=command_help)
@click.option('--packing_type', type=click.Choice(['unreal_pak', 'repak', 'engine', 'loose']), help='Packing type for the mod.', required=True, default='unreal_pak')
@click.option('--mod_name_dir_type', type=str, default='Mods', help='Directory type for the mod name (default: "Mods").')
@click.option('--use_mod_name_dir_name_override', type=bool, default=False, help='Whether to override the mod name directory (default: False).')
@click.option('--mod_name_dir_name_override', type=str, default=None, help='Override the mod name directory with this value (optional).')
@click.option('--pak_chunk_num', type=int, default=None, help='Pak chunk number (optional).')
@click.option('--compression_type', default='', type=str, help='Compression type for the mod (optional).')
@click.option('--is_enabled', type=bool, default=True, help='Whether the mod is enabled (default: True).')
@click.option(
    '--asset_paths', 
    multiple=True, 
    help='Asset path for the mod, can be specified multiple times.', 
    type=click.Path(
        exists=True, 
        file_okay=True, 
        dir_okay=False, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.option(
    '--tree_paths', 
    multiple=True, 
    help='Tree path for the mod, can be specified multiple times.', 
    type=click.Path(
        exists=True, 
        file_okay=False, 
        dir_okay=True, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    )
)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
@click.argument('mod_name', type=str)
@click.argument('pak_dir_structure', type=str)
def add_mod(
    settings_json, 
    mod_name, 
    packing_type, 
    pak_dir_structure,
    mod_name_dir_type, 
    use_mod_name_dir_name_override, 
    mod_name_dir_name_override, 
    pak_chunk_num, 
    compression_type, 
    is_enabled, 
    asset_paths, 
    tree_paths
):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
        mod_name (str): The name of the mod to add.
        pak_dir_structure (str): Path to the directory structure for packing.
    """
    main_logic.add_mod(
        settings_json, 
        mod_name, packing_type, 
        pak_dir_structure, 
        mod_name_dir_type, 
        use_mod_name_dir_name_override, 
        mod_name_dir_name_override, 
        pak_chunk_num, 
        compression_type, 
        is_enabled, 
        asset_paths, 
        tree_paths
    )


command_help = 'Removes the given mod names in the provided settings JSON.'
@cli.command(name='remove_mods', help=command_help, short_help=command_help)
@click.option("--mod_names", multiple=True, type=str, required=True, help='Name of a mod to be removed, can be specified multiple times')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def remove_mods(settings_json, mod_names):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.remove_mods(settings_json, mod_names)


command_help = 'Run the game.'
@cli.command(name='run_game', help=command_help, short_help=command_help)
@click.option('--toggle_engine', default=False, type=bool, help='Whether to close engine instances at the start and open at the end of the command process (default: False).')
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def run_game(settings_json, toggle_engine):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.run_game(settings_json, toggle_engine)


command_help = 'Close the game.'
@cli.command(name='close_game', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def close_game(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.close_game(settings_json)


command_help = 'Run the engine.'
@cli.command(name='run_engine', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def run_engine(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.run_engine(settings_json)


command_help = 'Close the engine.'
@cli.command(name='close_engine', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def close_engine(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.close_engine(settings_json)


command_help = 'Generates a uproject file at the specified location, using the given information.'
@cli.command(name='generate_uproject', help=command_help, short_help=command_help)
@click.option('--file_version', default=3, type=int, help='Uproject file specification. Defaults to 3.')
@click.option('--engine_major_association', default=4, type=int, help='Major Unreal Engine version for the project. Example: the 4 in 4.27.')
@click.option('--engine_minor_association', default=27, type=int, help='Minor Unreal Engine version for the project. Example: the 27 in 4.27.')
@click.option('--category', default='Modding', type=str, help='Category for the uproject.')
@click.option('--description', default='Uproject for modding, generated with unreal_auto_mod.', type=str, help='Description for the uproject.')
@click.option('--ignore_safety_checks', default=False, type=bool, help='Whether or not to override the input checks for this command.')
@click.argument('project_file', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def generate_uproject(project_file, file_version, engine_major_association, engine_minor_association, category, description, ignore_safety_checks):
    """
    Arguments:
        project_file (str): Path to generate the project file at.
    """
    main_logic.generate_uproject(project_file, file_version, engine_major_association, engine_minor_association, category, description, ignore_safety_checks)


host_type_choices = data_structures.get_enum_strings_from_enum(data_structures.UnrealHostTypes)
loading_phase_choices = data_structures.get_enum_strings_from_enum(data_structures.LoadingPhases)

command_help = 'Adds the specified module entry to the descriptor file, overwriting if it already exists.'
@cli.command(name='add_module_to_descriptor', help=command_help, short_help=command_help)
@click.option('--host_type', type=click.Choice(host_type_choices), default=data_structures.UnrealHostTypes.DEVELOPER.value, required=True, help='The host type to use.')
@click.option('--loading_phase', type=click.Choice(loading_phase_choices), default=data_structures.LoadingPhases.DEFAULT.value, required=True, help='The loading phase to use.')
@click.argument('descriptor_file', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
@click.argument('module_name', type=str)
def add_module_to_descriptor(descriptor_file, module_name, host_type, loading_phase):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the module to.
        module_name (str): Name of the module to add.
    """
    main_logic.add_module_to_descriptor(descriptor_file, module_name, host_type, loading_phase)


command_help = 'Adds the specified plugin entry to the descriptor file, overwriting if it already exists.'
@cli.command(name='add_plugin_to_descriptor', help=command_help, short_help=command_help)
@click.option('--is_enabled', default=True, type=bool, help='Whether or not Enabled is ticked for the plugin entry.')
@click.argument('descriptor_file', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
@click.argument('plugin_name', type=str)
def add_plugin_to_descriptor(descriptor_file, plugin_name, is_enabled):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to add the plugin to.
        plugin_name (str): Name of the plugin to add.
    """
    main_logic.add_plugin_to_descriptor(descriptor_file, plugin_name, is_enabled)


command_help = 'Removes the module name entries in the provided descriptor file if they exist.'
@cli.command(name='remove_modules_from_descriptor', help=command_help, short_help=command_help)
@click.option("--module_names", multiple=True, type=str, required=True, help='A module name to remove from the descriptor file, can be specified multiple times.')
@click.argument('descriptor_file', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def remove_modules_from_descriptor(descriptor_file, module_names):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the modules from.
    """
    main_logic.remove_modules_from_descriptor(descriptor_file, module_names)


command_help = 'Removes the plugin name entries in the provided descriptor file if they exist.'
@cli.command(name='remove_plugins_from_descriptor', help=command_help, short_help=command_help)
@click.option("--plugin_names", multiple=True, type=str, required=True, help='A plugin name to remove from the descriptor file, can be specified multiple times.')
@click.argument('descriptor_file', type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def remove_plugins_from_descriptor(descriptor_file, plugin_names):
    """
    Arguments:
        descriptor_file (str): Path to the descriptor file to remove the plugins from.
    """
    main_logic.remove_plugins_from_descriptor(descriptor_file, plugin_names)


command_help = 'Generates a uplugin in a directory, within the specified directory with the given settings.'
@cli.command(name='generate_uplugin', help=command_help, short_help=command_help)
@click.option('--can_contain_content', default=True, type=bool, help='Whether the plugin can contain content.')
@click.option('--is_installed', default=True, type=bool, help='Whether the plugin is installed.')
@click.option('--is_hidden', default=False, type=bool, help='Whether the plugin is hidden.')
@click.option('--no_code', default=False, type=bool, help='Whether the plugin should contain code.')
@click.option('--category', default='Modding', type=str, help='Category for the plugin.')
@click.option('--created_by', default='', type=str, help='Name of the creator of the plugin.')
@click.option('--created_by_url', default='', type=str, help='URL of the creator of the plugin.')
@click.option('--description', default='', type=str, help='Description of the plugin.')
@click.option('--docs_url', default='', type=str, help='Documentation URL for the plugin.')
@click.option('--editor_custom_virtual_path', default='', type=str, help='Custom virtual path for the editor.')
@click.option('--enabled_by_default', default=True, type=str, help='Whether the plugin is enabled by default.')
@click.option('--engine_major_version', default=4, type=int, help='Major Unreal Engine version for the plugin.')
@click.option('--engine_minor_version', default=27, type=int, help='Minor Unreal Engine version for the plugin.')
@click.option('--support_url', default='', type=str, help='Support URL for the plugin.')
@click.option('--version', default=1.0, type=float, help='Version of the plugin.')
@click.option('--version_name', default='', type=str, help='Version name of the plugin.')
@click.argument('plugins_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
@click.argument('plugin_name', type=str)
def generate_uplugin(
    plugins_directory, 
    plugin_name, 
    can_contain_content, 
    is_installed, 
    is_hidden, 
    no_code, 
    category, 
    created_by, 
    created_by_url, 
    description, 
    docs_url, 
    editor_custom_virtual_path, 
    enabled_by_default, 
    engine_major_version, 
    engine_minor_version, 
    support_url, 
    version, 
    version_name
    ):
    """
    Arguments:
        plugins_directory (str): Path to the plugins directory, mainly for use with Uproject plugins folder, and engine plugins folder.
        plugin_name (str): Name of the plugin to be generated.
    """
    main_logic.generate_uplugin(
        plugins_directory, 
        plugin_name, 
        can_contain_content, 
        is_installed, 
        is_hidden, 
        no_code, 
        category, 
        created_by, 
        created_by_url, 
        description, 
        docs_url, 
        editor_custom_virtual_path, 
        enabled_by_default, 
        engine_major_version, 
        engine_minor_version, 
        support_url, 
        version, 
        version_name
    )


command_help = 'Deletes all files for the specified uplugin paths.'
@cli.command(name='remove_uplugins', help=command_help, short_help=command_help)
@click.option(
    "--uplugin_paths", 
    multiple=True, 
    type=click.Path(
        exists=True, 
        file_okay=True, 
        dir_okay=False, 
        readable=True, 
        resolve_path=True, 
        path_type=pathlib.Path
    ), 
    required=True, 
    help='uplugin_paths: A path to a uplugin to delete, can be specified multiple times.'
)
def remove_uplugins(uplugin_paths):
    main_logic.remove_uplugins(uplugin_paths)


command_help = 'Resaves packages and fixes up redirectors for the project.'
@cli.command(name='resave_packages_and_fix_up_redirectors', help=command_help, short_help=command_help)
@click.argument("settings_json", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True, path_type=pathlib.Path))
def resave_packages_and_fix_up_redirectors(settings_json):
    """
    Arguments:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.resave_packages_and_fix_up_redirectors(settings_json)


command_help = 'Closes all programs with the exe names provided.'
@cli.command(name='close_programs', help=command_help, short_help=command_help)
@click.option("--exe_names", multiple=True, type=str, required=True, help='Name of an executable to be closed, can be specified multiple times.')
def close_programs(exe_names):
    main_logic.close_programs(exe_names)


command_help = 'Install Fmodel.'
@cli.command(name='install_fmodel', help=command_help, short_help=command_help)
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def install_fmodel(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_fmodel(output_directory, run_after_install)


command_help = 'Install Umodel.'
@cli.command(name='install_umodel', help=command_help, short_help=command_help)
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def install_umodel(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_umodel(output_directory, run_after_install)


command_help = 'Install Stove.'
@cli.command(name='install_stove', help=command_help, short_help=command_help)
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
def install_stove(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_stove(output_directory, run_after_install)


command_help = 'Install Spaghetti.'
@cli.command(name='install_spaghetti', help=command_help, short_help=command_help)
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def install_spaghetti(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_spaghetti(output_directory, run_after_install)


command_help = 'Install UAssetGUI.'
@cli.command(name='install_uasset_gui', help=command_help, short_help=command_help)
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def install_uasset_gui(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_uasset_gui(output_directory, run_after_install)


command_help = 'Install Kismet Analyzer.'
@cli.command(name='install_kismet_analyzer', help=command_help, short_help=command_help)
@click.option('--run_after_install', is_flag=True, default=False, type=bool, help='Should the installed program be run after installation.')
@click.argument('output_directory', type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path))
def install_kismet_analyzer(output_directory, run_after_install):
    """
    Arguments:
        output_directory (str): Path to the output directory
    """
    main_logic.install_kismet_analyzer(output_directory, run_after_install)
