import os

import psutil

from unreal_auto_mod import file_io, settings
from unreal_auto_mod.data_structures import HookStateType
from unreal_auto_mod.programs import unreal_engine


def get_process_name(exe_path: str) -> str:
    filename = os.path.basename(exe_path)
    return filename


def is_process_running(process_name: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def kill_process(process_name: str):
    os.system(f'taskkill /f /im "{process_name}"')


def get_processes_by_substring(substring: str) -> list:
    all_processes = psutil.process_iter(['pid', 'name'])
    matching_processes = [proc.info for proc in all_processes if substring.lower() in proc.info['name'].lower()]
    return matching_processes


def get_process_kill_events() -> list:
    return settings.settings_information.settings['process_kill_events']['processes']


def kill_processes(state: HookStateType):
    current_state = state.value if isinstance(state, HookStateType) else state
    for process_info in get_process_kill_events():
        target_state = process_info.get('hook_state')
        if target_state == current_state:
            if process_info['use_substring_check']:
                proc_name_substring = process_info['process_name']
                for proc_info in get_processes_by_substring(proc_name_substring):
                    proc_name = proc_info['name']
                    kill_process(proc_name)
            else:
                proc_name = process_info['process_name']
                kill_process(proc_name)


def get_game_process_name():
    return unreal_engine.get_game_process_name(settings.get_game_exe_path())


def close_programs(exe_names: list[str]):
    results = {}

    for exe_name in exe_names:
        found = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == exe_name.lower():
                    proc.terminate()
                    proc.wait(timeout=5)
                    found = True
                    results[exe_name] = "Closed"
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
        if not found:
            results[exe_name] = "Not Found"

    return results
