from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Optional

from unreal_auto_mod import app_runner, log, process_management, settings, timer, window_management
from unreal_auto_mod.app_runner import ExecutionMode
from unreal_auto_mod.enums import get_enum_from_val
from unreal_auto_mod.window_management import WindowAction


class HookStateType(Enum):
    """
    enum for the various hook states, used to fire off other functions
    at specific times, constant and init are not for use with the hook_state_decorator
    """
    CONSTANT = 'constant'
    INIT = 'init'

    PRE_ALL = 'pre_all'
    POST_ALL = 'post_all'
    PRE_INIT = 'pre_init'
    POST_INIT = 'post_init'
    PRE_COOKING = 'pre_cooking'
    POST_COOKING = 'post_cooking'
    PRE_MODS_UNINSTALL = 'pre_mods_uninstall'
    POST_MODS_UNINSTALL = 'post_mods_uninstall'
    PRE_PAK_DIR_SETUP = 'pre_pak_dir_setup'
    POST_PAK_DIR_SETUP = 'post_pak_dir_setup'
    PRE_MODS_INSTALL = 'pre_mods_install'
    POST_MODS_INSTALL = 'post_mods_install'
    PRE_GAME_LAUNCH = 'pre_game_launch'
    POST_GAME_LAUNCH = 'post_game_launch'
    PRE_GAME_CLOSE = 'pre_game_close'
    POST_GAME_CLOSE = 'post_game_close'
    PRE_ENGINE_OPEN = 'pre_engine_open'
    POST_ENGINE_OPEN = 'post_engine_open'
    PRE_ENGINE_CLOSE = 'pre_engine_close'
    POST_ENGINE_CLOSE = 'post_engine_close'
    PRE_CLEANUP = 'pre_cleanup'
    POST_CLEANUP = 'post_cleanup'
    PRE_CHANGES_UPLOAD = 'pre_changes_upload'
    POST_CHANGES_UPLOAD = 'post_changes_upload'
    PRE_BUILD_UPROJECT = 'pre_uproject_build'
    POST_BUILD_UPROJECT = 'post_uproject_build'
    PRE_GENERATE_MOD_RELEASE = 'pre_generate_mod_release'
    POST_GENERATE_MOD_RELEASE = 'post_generate_mod_release'
    PRE_GENERATE_MOD_RELEASES = 'pre_generate_mod_releases'
    POST_GENERATE_MOD_RELEASES = 'post_generate_mod_releases'
    PRE_GENERATE_MOD = 'pre_generate_mod'
    POST_GENERATE_MOD = 'post_generate_mod'
    PRE_GENERATE_MODS = 'pre_generate_mods'
    POST_GENERATE_MODS = 'post_generate_mods'


@dataclass
class HookStateInfo:
    hook_state: HookStateType


hook_state_info = HookStateInfo(HookStateType.PRE_INIT)


def exec_events_checks(hook_state_type: HookStateType):
    exec_events = settings.get_exec_events()
    for exec_event in exec_events:
        value = exec_event['hook_state']
        exe_state = get_enum_from_val(HookStateType, value)
        if exe_state == hook_state_type:
            exe_path = exec_event['alt_exe_path']
            exe_args = exec_event['variable_args']
            exe_exec_mode = get_enum_from_val(ExecutionMode, exec_event['execution_mode'])
            app_runner.run_app(exe_path, exe_exec_mode, exe_args)


def is_hook_state_used(state: HookStateType) -> bool:
    if isinstance(settings.settings_information.settings, dict):
        if "process_kill_events" in settings.settings_information.settings:
            process_kill_events = settings.settings_information.settings.get("process_kill_events", {})
            if "processes" in process_kill_events:
                for process in process_kill_events["processes"]:
                    if isinstance(state, HookStateType):
                        state = state.value
                    if process.get('hook_state') == state:
                        return True

        if "window_management_events" in settings.settings_information.settings:
            for window in settings.get_window_management_events():
                if isinstance(state, HookStateType):
                    state = state.value
                if window.get("hook_state") == state:
                    return True

        if "exec_events" in settings.settings_information.settings:
            for method in settings.get_exec_events():
                if isinstance(state, HookStateType):
                    state = state.value
                if method.get("hook_state") == state:
                    return True

    return False


def window_checks(current_state: WindowAction):
    window_settings_list = settings.get_window_management_events()
    for window_settings in window_settings_list:
        settings_state = get_enum_from_val(HookStateType, window_settings['hook_state'])
        if settings_state == current_state:
            title = window_settings['window_name']
            windows_to_change = window_management.get_windows_by_title(title, use_substring_check=window_settings['use_substring_check'])
            for window_to_change in windows_to_change:
                way_to_change_window = get_enum_from_val(WindowAction, window_settings['window_behaviour'])
                if way_to_change_window == WindowAction.MAX:
                    window_management.maximize_window(window_to_change)
                elif way_to_change_window == WindowAction.MIN:
                    window_management.minimize_window(window_to_change)
                elif way_to_change_window == WindowAction.CLOSE:
                    window_management.close_window(window_to_change)
                elif way_to_change_window == WindowAction.MOVE:
                    window_management.move_window(window_to_change, window_settings)
                else:
                    log.log_message('Monitor: invalid window behavior specified in settings')


def hook_state_checks(hook_state: HookStateType):
    if hook_state != HookStateType.CONSTANT:
        log.log_message(f'Hook State Check: {hook_state} is running')
    if is_hook_state_used(hook_state):
        process_management.kill_processes(hook_state)
        window_checks(hook_state)
        exec_events_checks(hook_state)
    if hook_state != HookStateType.CONSTANT:
        log.log_message(f'Hook State Check: {hook_state} finished')


def set_hook_state(new_state: HookStateType):
    hook_state_info.hook_state = new_state
    log.log_message(f'Hook State: changed to {new_state}')
    # calling this on preinit causes problems so will avoid for now
    if new_state != HookStateType.PRE_INIT:
        hook_state_checks(HookStateType.PRE_ALL)
        hook_state_checks(new_state)
        hook_state_checks(HookStateType.POST_ALL)
        log.log_message(f'Timer: Time since script execution: {timer.get_running_time()}')



def hook_state_decorator(
    start_hook_state_type: HookStateType,
    end_hook_state_type: Optional[HookStateType] = None
):
    def decorator(function: Callable[..., Any]):
        def wrapper(*args, **kwargs):
            set_hook_state(start_hook_state_type)
            result = function(*args, **kwargs)
            if end_hook_state_type is not None:
                set_hook_state(end_hook_state_type)
            return result
        return wrapper
    return decorator
