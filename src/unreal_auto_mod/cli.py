import os
import click
from trogon import tui

from unreal_auto_mod import (
    data_structures,
    main_logic,
    file_io,
    _version
)


default_releases_dir = os.path.normpath(os.path.join(main_logic.settings_json_dir, 'mod_packaging', 'releases'))
default_output_releases_dir = os.path.normpath(os.path.join(file_io.SCRIPT_DIR, 'dist'))


@tui()
@click.version_option(version=_version.version)
@click.group(chain=True)
def cli():
    pass

@cli.command(name='build')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def build(settings_json, toggle_engine):
    """
    Builds the uproject specified within the settings JSON

    Args:
        settings_json (string): Path to the settings JSON file
        toggle_engine (bool): Will close engine instances at the start and open at the end of the command process
    """
    main_logic.build(settings_json, toggle_engine)

@cli.command(name='cook')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def cook(settings_json, toggle_engine):
    """
    Cooks content for the uproject specified within the settings JSON

    Args:
        settings_json (string): Path to the settings JSON file
        toggle_engine (bool): Will close engine instances at the start and open at the end of the command process
    """
    main_logic.cook(settings_json, toggle_engine)

@cli.command(name='package')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def package(settings_json, toggle_engine, use_symlinks):
    """
    Package content for the uproject specified within the settings JSON

    Args:
        settings_json (string): Path to the settings JSON file
        toggle_engine (bool): Wether or not to close engine instances at the start and open at the end of the command process
        use_symlinks (bool): Wether or not to use symlinks to save time with file operations
    """
    main_logic.package(settings_json, toggle_engine, use_symlinks)

@cli.command(name='test_mods')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def test_mods(settings_json, mod_names, toggle_engine, use_symlinks):
    """
    Run tests for specific mods

    Args:
        settings_json (string): Path to the settings JSON file
        mod_names (list): List of mod names
        toggle_engine (bool): Wether or not to close engine instances at the start and open at the end of the command process
        use_symlinks (bool): Wether or not to use symlinks to save time with file operations
    """
    main_logic.test_mods(settings_json, mod_names, toggle_engine, use_symlinks)

@cli.command(name='test_mods_all')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def test_mods_all(settings_json, toggle_engine, use_symlinks):
    """
    Run tests for all mods within the specified settings JSON

    Args:
        settings_json (string): Path to the settings JSON file
        toggle_engine (bool): Wether or not to close engine instances at the start and open at the end of the command process
        use_symlinks (bool): Wether or not to use symlinks to save time with file operations
    """
    main_logic.test_mods_all(settings_json, toggle_engine, use_symlinks)

@cli.command(name='full_run')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.option("--base_files_directory", default=default_releases_dir)
@click.option("--output_directory", default=default_output_releases_dir)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def full_run_all(settings_json, mod_names, toggle_engine, base_files_directory, output_directory, use_symlinks):
    """
    Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for the specified mod names.

    Args:
        settings_json (str): Path to the settings JSON file
        mod_names (list): List of mod names
        toggle_engine (bool): Will close engine instances at the start and open at the end of the command process
        base_files_directory (str): Path to dir tree whose content to pack alongside the mod for release
        output_directory (str): Path to the output directory
        use_symlinks (bool): Whether or not to use symlinks to save time with file operations
    """
    main_logic.full_run(settings_json, mod_names, toggle_engine, base_files_directory, output_directory, use_symlinks)

@cli.command(name='full_run_all', help='Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for the specified mod names.')
@click.option("--toggle_engine", is_flag=True, default=False, type=bool)
@click.option("--base_files_directory", default=default_releases_dir)
@click.option("--output_directory", default=default_output_releases_dir)
@click.option("--use_symlinks", is_flag=True, default=False, type=bool)
@click.argument("settings_json", type=str)
def full_run_all(settings_json, toggle_engine, base_files_directory, output_directory, use_symlinks):
    """
    Builds, Cooks, Packages, Generates Mods, and Generates Mod Releases for the specified mod names.

    Args:
        settings_json (str): Path to the settings JSON file
        toggle_engine (bool): Will close engine instances at the start and open at the end of the command process
        base_files_directory (str): Path to dir tree whose content to pack alongside the mod for release
        output_directory (str): Path to the output directory
        use_symlinks (bool): Whether or not to use symlinks to save time with file operations
    """
    main_logic.full_run_all(settings_json, toggle_engine, base_files_directory, output_directory, use_symlinks)

@cli.command(name='generate_mods')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.option('--use_symlinks', is_flag=True, default=False, type=bool)
@click.argument('settings_json', type=str)
def generate_mods(settings_json, mod_names, use_symlinks):
    """
    Generates mods for the specified mod names.

    Args:
        settings_json (str): Path to the settings JSON file
        mod_names (list): List of mod names
        use_symlinks (bool): Whether or not to use symlinks to save time with file operations
    """
    main_logic.generate_mods(settings_json, mod_names, use_symlinks)

@cli.command(name='generate_mods_all')
@click.option('--use_symlinks', is_flag=True, default=False, type=bool)
@click.argument('settings_json', type=str)
def generate_mods_all(settings_json, use_symlinks):
    """
    Generates mods for all enabled mods within the specified settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file
        use_symlinks (bool): Whether or not to use symlinks to save time with file operations
    """
    main_logic.generate_mods_all(settings_json, use_symlinks)

@cli.command(name='generate_mod_releases')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.option('--base_files_directory', default=default_releases_dir, type=str)
@click.option('--output_directory', default=default_output_releases_dir, type=str)
@click.argument('settings_json', type=str)
def generate_mod_releases(settings_json, mod_names, base_files_directory, output_directory):
    """
    Generate one or more mod releases.

    Args:
        settings_json (str): Path to the settings JSON file.
        mod_names (list): List of mod names.
        base_files_directory (str, optional): Path to directory tree whose content to pack alongside the mod for release.
        output_directory (str, optional): Path to the output directory.
    """
    main_logic.generate_mod_releases(settings_json, mod_names, base_files_directory, output_directory)

@cli.command(name='generate_mod_releases_all')
@click.option('--base_files_directory', default=default_releases_dir, type=str)
@click.option('--output_directory', default=default_output_releases_dir, type=str)
@click.argument('settings_json', type=str)
def generate_mod_releases_all(settings_json, base_files_directory, output_directory):
    """
    Generate mod releases for all mods within the specified settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
        base_files_directory (str, optional): Path to directory tree whose content to pack alongside the mod for release.
        output_directory (str, optional): Path to the output directory.
    """
    main_logic.generate_mod_releases_all(settings_json, base_files_directory, output_directory)

@cli.command(name='cleanup_full')
@click.argument('settings_json', type=str)
def cleanup_full(settings_json):
    """
    Cleans up the GitHub repository specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_full(settings_json)

@cli.command(name='cleanup_cooked')
@click.argument('settings_json', type=str)
def cleanup_cooked(settings_json):
    """
    Cleans up the directories made from cooking of the GitHub repository specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_cooked(settings_json)

@cli.command(name='cleanup_build')
@click.argument('settings_json', type=str)
def cleanup_build(settings_json):
    """
    Cleans up the directories made from building of the GitHub repository specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_build(settings_json)

@cli.command(name='cleanup_game')
@click.argument('settings_json', type=str)
def cleanup_game(settings_json):
    """
    Cleans up the specified directory, deleting all files not specified within the file list JSON.
    
    To generate a file list JSON, use the generate_file_list_json command.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.cleanup_game(settings_json)
@cli.command(name='generate_game_file_list_json')
@click.argument('settings_json', type=str)
def generate_game_file_list_json(settings_json):
    """
    Generates a JSON file containing all of the files in the game directory, from the game exe specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.generate_game_file_list_json(settings_json)

@cli.command(name='cleanup_from_file_list')
@click.argument('file_list', type=str)
@click.argument('directory', type=str)
def cleanup_from_file_list(file_list, directory):
    """
    Cleans up the specified directory, deleting all files not specified within the file list JSON.
    
    To generate one, use the generate_file_list command.

    Args:
        file_list (str): Path to the file list you want to clean from.
        directory (str): Path to the directory tree to clean up. It will delete all files not in the specified file list.
    """
    main_logic.cleanup_from_file_list(file_list, directory)

@cli.command(name='generate_file_list')
@click.argument('directory', type=str)
@click.argument('file_list', type=str)
def generate_file_list(directory, file_list):
    """
    Generates a JSON file containing all of the files in the specified directory.

    Args:
        directory (str): Path to the directory tree you want to generate the file list from.
        file_list (str): Path to the output file, saved in JSON format.
    """
    main_logic.generate_file_list(directory, file_list)

@cli.command(name='upload_changes_to_repo')
@click.argument('settings_json', type=str)
def upload_changes_to_repo(settings_json):
    """
    Uploads the latest changes of the git project to the GitHub repository and branch specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.upload_changes_to_repo(settings_json)

@cli.command(name='resync_dir_with_repo')
@click.argument('settings_json', type=str)
def resync_dir_with_repo(settings_json):
    """
    Cleans up and resyncs a git project to the GitHub repository and branch specified within the settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.resync_dir_with_repo(settings_json)

@cli.command(name='open_latest_log')
@click.argument('settings_json', type=str)
def open_latest_log(settings_json):
    """
    Opens the latest log file.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.open_latest_log(settings_json)

@cli.command(name='enable_mods')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.argument('settings_json', type=str)
def enable_mods(settings_json, mod_names):
    """
    Enable the given mod names in the provided settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
        mod_names (list): List of mod names to be enabled.
    """
    main_logic.enable_mods(settings_json, mod_names)

@cli.command(name='disable_mods')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.argument('settings_json', type=str)
def disable_mods(settings_json, mod_names):
    """
    Disable the given mod names in the provided settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
        mod_names (list): List of mod names to be disabled.
    """
    main_logic.disable_mods(settings_json, mod_names)
    
@cli.command(name='add_mod')
@click.option('--packing_type', type=click.Choice(['unreal_pak', 'repak', 'engine', 'loose']), help='Packing type for the mod.', required=True, default='unreal_pak')
@click.option('--mod_name_dir_type', type=str, default='Mods')
@click.option('--use_mod_name_dir_name_override', type=bool, default=False)
@click.option('--mod_name_dir_name_override', type=str, default=None)
@click.option('--pak_chunk_num', type=int, default=None)
@click.option('--compression_type', default='', type=str)
@click.option('--is_enabled', type=bool, default=True)
@click.option('--asset_paths', type=str, multiple=True)
@click.option('--tree_paths', type=str, multiple=True)
@click.argument('settings_json', type=str)
@click.argument('mod_name', type=str)
@click.argument('pak_dir_structure', type=str)
def add_mod(settings_json, mod_name, packing_type, pak_dir_structure, mod_name_dir_type, use_mod_name_dir_name_override, mod_name_dir_name_override, pak_chunk_num, compression_type, is_enabled, asset_paths, tree_paths):
    """
    Adds the given mod name in the provided settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
        mod_name (str): The name of the mod to add.
        packing_type (str): The type of packing for the mod.
        pak_dir_structure (str): Path to the directory structure for packing.
        mod_name_dir_type (str): Directory type for the mod name (default: 'Mods').
        use_mod_name_dir_name_override (bool): Whether to override the mod name directory (default: False).
        mod_name_dir_name_override (str): Override the mod name directory with this value (optional).
        pak_chunk_num (int): Pak chunk number (optional).
        compression_type (str): Compression type for the mod (optional).
        is_enabled (bool): Whether the mod is enabled (default: True).
        asset_paths (list): Asset paths for the mod (default: empty list).
        tree_paths (list): Tree paths for the mod (default: empty list).
    """
    main_logic.add_mod(settings_json, mod_name, packing_type, pak_dir_structure, mod_name_dir_type, use_mod_name_dir_name_override, mod_name_dir_name_override, pak_chunk_num, compression_type, is_enabled, asset_paths, tree_paths)


@cli.command(name='remove_mods')
@click.option("--mod_names", multiple=True, type=list[str], required=True)
@click.argument('settings_json', type=str)
def remove_mods(settings_json, mod_names):
    """
    Removes the given mod names in the provided settings JSON.

    Args:
        settings_json (str): Path to the settings JSON file.
        mod_names (list): List of mod names to be removed.
    """
    main_logic.remove_mods(settings_json, mod_names)

@cli.command(name='run_game')
@click.option('--toggle_engine', default=False, type=bool)
@click.argument('settings_json', type=str)
def run_game(settings_json, toggle_engine):
    """
    Run the game.

    Args:
        settings_json (str): Path to the settings JSON file.
        toggle_engine (bool): Whether to close engine instances at the start and open at the end of the command process (default: False).
    """
    main_logic.run_game(settings_json, toggle_engine)

@cli.command(name='close_game')
@click.argument('settings_json', type=str)
def close_game(settings_json):
    """
    Close the game.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.close_game(settings_json)

@cli.command(name='run_engine')
@click.argument('settings_json', type=str)
def run_engine(settings_json):
    """
    Run the engine.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.run_engine(settings_json)

@cli.command(name='close_engine')
@click.argument('settings_json', type=str)
def close_engine(settings_json):
    """
    Close the engine.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.close_engine(settings_json)

@cli.command(name='generate_uproject')
@click.option('--file_version', default=3, type=int)
@click.option('--engine_major_association', default=4, type=int)
@click.option('--engine_minor_association', default=27, type=int)
@click.option('--category', default='Modding', type=str)
@click.option('--description', default='Uproject for modding, generated with unreal_auto_mod.', type=str)
@click.option('--modules', type=str, multiple=True)
@click.option('--plugins', type=str, multiple=True)
@click.option('--ignore_safety_checks', default=False, type=bool)
@click.argument('project_file', type=str)
def generate_uproject(project_file, file_version, engine_major_association, engine_minor_association, category, description, modules, plugins, ignore_safety_checks):
    """
    Generates a uproject file at the specified location, using the given information.

    Args:
        project_file (str): Path to generate the project file at.
        file_version (int): Uproject file specification. Defaults to 3.
        engine_major_association (int): Major Unreal Engine version for the project. Example: the 4 in 4.27.
        engine_minor_association (int): Minor Unreal Engine version for the project. Example: the 27 in 4.27.
        category (str): Category for the uproject.
        description (str): Description for the uproject.
        modules (dict): Modules for the uproject.
        plugins (dict): Plugins for the uproject.
        ignore_safety_checks (bool): Whether or not to override the input checks for this command.
    """
    main_logic.generate_uproject(project_file, file_version, engine_major_association, engine_minor_association, category, description, modules, plugins, ignore_safety_checks)

host_type_choices = data_structures.get_enum_strings_from_enum(data_structures.UnrealHostTypes)
loading_phase_choices = data_structures.get_enum_strings_from_enum(data_structures.LoadingPhases)

@cli.command(name='add_module_to_descriptor')
@click.option('--host_type', type=click.Choice(host_type_choices), default=data_structures.UnrealHostTypes.DEVELOPER.value, required=True)
@click.option('--loading_phase', type=click.Choice(loading_phase_choices), default=data_structures.LoadingPhases.DEFAULT.value, required=True)
@click.argument('descriptor_file', type=str)
@click.argument('module_name', type=str)
def add_module_to_descriptor(descriptor_file, module_name, host_type, loading_phase):
    """
    Adds the specified module entry to the descriptor file, overwriting if it already exists.

    Args:
        descriptor_file (str): Path to the descriptor file to add the module to.
        module_name (str): Name of the module to add.
        host_type (str): The host type to use.
        loading_phase (str): The loading phase to use.
    """
    main_logic.add_module_to_descriptor(descriptor_file, module_name, host_type, loading_phase)

@cli.command(name='add_plugin_to_descriptor')
@click.option('--is_enabled', default=True, type=bool)
@click.argument('descriptor_file', type=str)
@click.argument('plugin_name', type=str)
def add_plugin_to_descriptor(descriptor_file, plugin_name, is_enabled):
    """
    Adds the specified plugin entry to the descriptor file, overwriting if it already exists.

    Args:
        descriptor_file (str): Path to the descriptor file to add the plugin to.
        plugin_name (str): Name of the plugin to add.
        is_enabled (bool): Whether or not Enabled is ticked for the plugin entry.
    """
    main_logic.add_plugin_to_descriptor(descriptor_file, plugin_name, is_enabled)

@cli.command(name='remove_modules_from_descriptor')
@click.option("--module_names", multiple=True, type=list[str], required=True)
@click.argument('descriptor_file', type=str)
def remove_modules_from_descriptor(descriptor_file, module_names):
    """
    Removes the module name entries in the provided descriptor file if they exist.

    Args:
        descriptor_file (str): Path to the descriptor file to remove the modules from.
        module_names (list): List of one or more module names to remove from the descriptor file.
    """
    main_logic.remove_modules_from_descriptor(descriptor_file, module_names)

@cli.command(name='remove_plugins_from_descriptor')
@click.option("--plugin_names", multiple=True, type=list[str], required=True)
@click.argument('descriptor_file', type=str)
def remove_plugins_from_descriptor(project_file, plugin_names):
    """
    Removes the plugin name entries in the provided descriptor file if they exist.

    Args:
        project_file (str): Path to the descriptor file to remove the plugins from.
        plugin_names (list): List of one or more plugin names to remove from the descriptor file.
    """
    main_logic.remove_plugins_from_descriptor(project_file, plugin_names)

@cli.command(name='generate_uplugin')
@click.option('--can_contain_content', default=True, type=bool)
@click.option('--is_installed', default=True, type=bool)
@click.option('--is_hidden', default=False, type=bool)
@click.option('--no_code', default=False, type=bool)
@click.option('--category', default='Modding', type=str)
@click.option('--created_by', default='', type=str)
@click.option('--created_by_url', default='', type=str)
@click.option('--description', default='', type=str)
@click.option('--docs_url', default='', type=str)
@click.option('--editor_custom_virtual_path', default='', type=str)
@click.option('--enabled_by_default', default=True, type=str)
@click.option('--engine_major_version', default=4, type=int)
@click.option('--engine_minor_version', default=27, type=int)
@click.option('--support_url', default='', type=str)
@click.option('--version', default=1.0, type=float)
@click.option('--version_name', default='', type=str)
@click.argument('plugins_directory', type=str)
@click.argument('plugin_name', type=str)
def generate_uplugin(plugins_directory, plugin_name, can_contain_content, is_installed, is_hidden, no_code, category, created_by, created_by_url, description, docs_url, editor_custom_virtual_path, enabled_by_default, engine_major_version, engine_minor_version, support_url, version, version_name):
    """
    Generates a uplugin in a directory, within the specified directory with the given settings.

    Args:
        plugins_directory (str): Path to the plugins directory, mainly for use with Uproject plugins folder, and engine plugins folder.
        plugin_name (str): Name of the plugin to be generated.
        can_contain_content (bool): Whether the plugin can contain content.
        is_installed (bool): Whether the plugin is installed.
        is_hidden (bool): Whether the plugin is hidden.
        no_code (bool): Whether the plugin should contain code.
        category (str): Category for the plugin.
        created_by (str): Name of the creator of the plugin.
        created_by_url (str): URL of the creator of the plugin.
        description (str): Description of the plugin.
        docs_url (str): Documentation URL for the plugin.
        editor_custom_virtual_path (str): Custom virtual path for the editor.
        enabled_by_default (str): Whether the plugin is enabled by default.
        engine_major_version (int): Major Unreal Engine version for the plugin.
        engine_minor_version (int): Minor Unreal Engine version for the plugin.
        support_url (str): Support URL for the plugin.
        version (float): Version of the plugin.
        version_name (str): Version name of the plugin.
    """
    main_logic.generate_uplugin(plugins_directory, plugin_name, can_contain_content, is_installed, is_hidden, no_code, category, created_by, created_by_url, description, docs_url, editor_custom_virtual_path, enabled_by_default, engine_major_version, engine_minor_version, support_url, version, version_name)

@cli.command(name='remove_uplugins')
@click.option("--uplugin_paths", multiple=True, type=list[str], required=True)
def remove_uplugins(uplugin_paths):
    """
    Deletes all files for the specified uplugin paths.

    Args:
        uplugin_paths (list): List of one or more uplugin paths to delete.
    """
    main_logic.remove_uplugins(uplugin_paths)

@cli.command(name='resave_packages_and_fix_up_redirectors')
@click.argument('settings_json', type=str)
def resave_packages_and_fix_up_redirectors(settings_json):
    """
    Resaves packages and fixes up redirectors for the project.

    Args:
        settings_json (str): Path to the settings JSON file.
    """
    main_logic.resave_packages_and_fix_up_redirectors(settings_json)

@cli.command(name='close_programs')
@click.option("--exe_names", multiple=True, type=list[str], required=True)
def close_programs(exe_names):
    """
    Closes all programs with the exe names provided.

    Args:
        exe_names (list): List of executable names to close.
    """
    main_logic.close_programs(exe_names)

@cli.command(name='install_fmodel')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_fmodel(output_directory, run_after_install):
    """
    Install Fmodel.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_fmodel(output_directory, run_after_install)

@cli.command(name='install_umodel')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_umodel(output_directory, run_after_install):
    """
    Install Umodel.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_umodel(output_directory, run_after_install)

@cli.command(name='install_stove')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_stove(output_directory, run_after_install):
    """
    Install Stove.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_stove(output_directory, run_after_install)

@cli.command(name='install_spaghetti')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_spaghetti(output_directory, run_after_install):
    """
    Install Spaghetti.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_spaghetti(output_directory, run_after_install)

@cli.command(name='install_uasset_gui')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_uasset_gui(output_directory, run_after_install):
    """
    Install UAssetGUI.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_uasset_gui(output_directory, run_after_install)

@cli.command(name='install_kismet_analyzer')
@click.option('--run_after_install', is_flag=True, default=False, type=bool)
@click.argument('output_directory', type=str)
def install_kismet_analyzer(output_directory, run_after_install):
    """
    Install Kismet Analyzer.

    Args:
        output_directory (str): Path to the output directory
        run_after_install (bool): Should the installed program be run after installation
    """
    main_logic.install_kismet_analyzer(output_directory, run_after_install)
