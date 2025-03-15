import json
import os
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List

from dynaconf import Dynaconf

from unreal_auto_mod import configs, file_io, logger, packing, process_management, settings, window_management
from unreal_auto_mod.logger import log_message
from unreal_auto_mod.programs import repak, unreal_engine


@dataclass
class SettingsInformation:
    settings: Dict[str, Any]
    init_settings_done: bool
    settings_json_dir: str
    program_dir: str
    mod_names: List[str]
    settings_json: str

settings_information = SettingsInformation(
    settings={},
    init_settings_done=False,
    settings_json_dir='',
    program_dir='',
    mod_names=[],
    settings_json=''
)


def init_settings(settings_json_path: pathlib.Path):
    raw_settings = Dynaconf(settings_files=[settings_json_path])
    settings_information.settings = configs.DynamicSettings(raw_settings)
    settings = settings_information.settings
    process_name = os.path.basename(settings['game_info']['game_exe_path'])
    window_management.change_window_name(settings['general_info']['window_title'])
    auto_close_game = settings['process_kill_events']['auto_close_game']
    is_process_running = process_management.is_process_running(process_name)
    if auto_close_game and is_process_running:
        os.system(f'taskkill /f /im "{process_name}"')
    settings_information.init_settings_done = True
    settings_information.settings_json = settings_json_path
    settings_information.settings_json_dir = os.path.dirname(settings_information.settings_json)


def check_file_exists(file_path: str) -> bool:
    if os.path.exists(file_path):
        return True
    else:
        raise FileNotFoundError(f'File "{file_path}" not found.')


def get_unreal_engine_dir() -> str:
    ue_dir = settings_information.settings['engine_info']['unreal_engine_dir']
    file_io.check_path_exists(ue_dir)
    return ue_dir


def unreal_engine_check():
    should_do_check = True

    if not packing.is_unreal_pak_packing_enum_in_use() or packing.is_engine_packing_enum_in_use():
           should_do_check = False

    if should_do_check:
        engine_str = 'UE4Editor'
        if unreal_engine.is_game_ue5(get_unreal_engine_dir()):
            engine_str = 'UnrealEditor'
        check_file_exists(f'{get_unreal_engine_dir()}/Engine/Binaries/Win64/{engine_str}.exe')
        logger.log_message('Check: Unreal Engine exists')


def get_game_exe_path() -> str:
    game_exe_path = settings_information.settings['game_info']['game_exe_path']
    return game_exe_path


def game_exe_check():
    check_file_exists(get_game_exe_path())


def get_git_info_repo_path() -> str:
    return settings_information.settings['git_info']['repo_path']


def git_info_check():
    git_repo_path = get_git_info_repo_path()
    if git_repo_path == None or git_repo_path == '':
        return

    check_file_exists(git_repo_path)


def get_game_launcher_exe_path() -> str:
    return settings_information.settings['game_info']['game_launcher_exe']


def get_override_automatic_launcher_exe_finding() -> bool:
    return settings_information.settings['game_info']['override_automatic_launcher_exe_finding']


def game_launcher_exe_override_check():
    if get_override_automatic_launcher_exe_finding():
        check_file_exists(get_game_launcher_exe_path())


def get_uproject_file() -> str:
    return settings_information.settings['engine_info']['unreal_project_file']


def uproject_check():
    uproject_file = get_uproject_file()
    if uproject_file:
        check_file_exists(uproject_file)
        logger.log_message('Check: Uproject file exists')


def init_checks():
    uproject_check()
    unreal_engine_check()
    game_launcher_exe_override_check()
    git_info_check()
    # game_exe_check()

    if repak.get_is_using_repak_path_override():
        check_file_exists(repak.get_repak_path_override())
        logger.log_message('Check: Repak exists')

    logger.log_message('Check: Game exists')

    logger.log_message('Check: Passed all init checks')


def load_settings(settings_json: str):
    log_message(f'settings json: {settings_json}')
    if not settings_information.init_settings_done:
        init_settings(settings_json)
    init_checks()


def get_unreal_engine_packaging_main_command() -> str:
    return settings_information.settings['engine_info']['engine_packaging_command']


def get_unreal_engine_cooking_main_command() -> str:
    return settings_information.settings['engine_info']['engine_cooking_command']


def get_unreal_engine_building_main_command() -> str:
    return settings_information.settings['engine_info']['engine_building_command']


def get_cleanup_repo_path() -> str:
    return settings_information.settings['git_info']['repo_path']


def get_window_title() -> str:
    return settings_information.settings['general_info']['window_title']


def get_window_title_override() -> str:
    return settings_information.settings['game_info']['window_title_override']


def get_override_automatic_window_title_finding() -> bool:
    return settings_information.settings['game_info']['override_automatic_window_title_finding']


def get_is_overriding_automatic_version_finding() -> bool:
    return settings_information.settings['repak_info']['override_automatic_version_finding']


def get_engine_building_args() -> list:
    return settings_information.settings['engine_info']['engine_building_args']


def get_engine_packaging_args() -> list:
    return settings_information.settings['engine_info']['engine_packaging_args']


def get_engine_cooking_args() -> list:
    return settings_information.settings['engine_info']['engine_cooking_args']


def get_window_management_events() -> dict:
    return settings_information.settings['window_management_events']


def get_override_working_dir() -> str:
    return settings_information.settings['general_info']['working_dir']


def get_is_overriding_default_working_dir() -> bool:
    return settings_information.settings['general_info']['override_default_working_dir']


def get_persistant_mod_dir(mod_name: str) -> str:
    return f'{settings_information.settings_json_dir}/mod_packaging/persistent_files/{mod_name}'


def get_persistent_mods_dir() -> str:
    return f'{settings_information.settings_json_dir}/mod_packaging/persistent_files'


def get_override_automatic_version_finding() -> bool:
    return settings_information.settings['engine_info']['override_automatic_version_finding']


def get_alt_packing_dir_name() -> str:
    return settings_information.settings['packaging_uproject_name']['name']


def get_is_using_alt_dir_name() -> bool:
    return settings_information.settings['packaging_uproject_name']['use_override']


def get_mods_info_list_from_json() -> list:
    return settings_information.settings['mods_info']


def get_exec_events() -> list:
    return settings_information.settings['exec_events']


def get_ide_path() -> str:
    return settings_information.settings['optionals']['ide_path']


def get_blender_path():
    return settings_information.settings['optionals']['blender_path']


def get_game_info_launch_type_enum_str_value() -> str:
    return settings_information.settings['game_info']['launch_type']


def get_game_id() -> int:
    return settings_information.settings['game_info']['game_id']


def get_game_launch_params() -> list:
    return settings_information.settings['game_info']['launch_params']


def get_engine_launch_args() -> list:
    return settings_information.settings['engine_info']['engine_launch_args']


def custom_get_unreal_engine_version(engine_path: str) -> str:
    if get_override_automatic_version_finding():
        unreal_engine_major_version = settings_information.settings['engine_info']['unreal_engine_major_version']
        unreal_engine_minor_version = settings_information.settings['engine_info']['unreal_engine_minor_version']
        return f'{unreal_engine_major_version}.{unreal_engine_minor_version}'
    else:
        return unreal_engine.get_unreal_engine_version(engine_path)


def get_working_dir() -> str:
    if settings.get_is_overriding_default_working_dir():
        working_dir = settings.get_override_working_dir()
    else:
        working_dir = os.path.join(file_io.SCRIPT_DIR, 'working_dir')
    os.makedirs(working_dir, exist_ok=True)
    return working_dir
