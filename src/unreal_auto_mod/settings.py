import json
import os
import pathlib
from dataclasses import dataclass
from typing import Any, Dict, List

from dynaconf import Dynaconf

from unreal_auto_mod import configs, log, process_management, unreal_engine, utilities, window_management
from unreal_auto_mod.log import log_message


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


def unreal_engine_check():
    should_do_check = True

    if not utilities.is_unreal_pak_packing_enum_in_use() or utilities.is_engine_packing_enum_in_use():
           should_do_check = False

    if should_do_check:
        engine_str = 'UE4Editor'
        if unreal_engine.is_game_ue5(utilities.get_unreal_engine_dir()):
            engine_str = 'UnrealEditor'
        check_file_exists(f'{utilities.get_unreal_engine_dir()}/Engine/Binaries/Win64/{engine_str}.exe')
        log.log_message('Check: Unreal Engine exists')


def game_exe_check():
    check_file_exists(utilities.get_game_exe_path())


def git_info_check():
    git_repo_path = utilities.get_git_info_repo_path()
    if git_repo_path == None or git_repo_path == '':
        return

    check_file_exists(git_repo_path)


def game_launcher_exe_override_check():
    if utilities.get_override_automatic_launcher_exe_finding():
        check_file_exists(utilities.get_game_launcher_exe_path())


def uproject_check():
    uproject_file = utilities.get_uproject_file()
    if uproject_file:
        check_file_exists(uproject_file)
        log.log_message('Check: Uproject file exists')


def init_checks():
    uproject_check()
    unreal_engine_check()
    game_launcher_exe_override_check()
    git_info_check()
    game_exe_check()

    if utilities.get_is_using_repak_path_override():
        check_file_exists(utilities.get_repak_path_override())
        log.log_message('Check: Repak exists')

    check_file_exists(utilities.get_game_exe_path())
    log.log_message('Check: Game exists')

    log.log_message('Check: Passed all init checks')


def load_settings(settings_json: str):
    log_message(f'settings json: {settings_json}')
    if not settings_information.init_settings_done:
        init_settings(settings_json)
    init_checks()


def save_settings(settings_json: str):
    with open(settings_json, 'w') as file:
        json.dump(settings_information.settings, file, indent=2)
