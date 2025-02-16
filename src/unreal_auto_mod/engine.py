from unreal_auto_mod import file_io as file_io, unreal_engine
from unreal_auto_mod import hook_states, thread_engine_monitor, utilities, log
from unreal_auto_mod.data_structures import ExecutionMode, HookStateType, PackagingDirType


@hook_states.hook_state_decorator(HookStateType.PRE_ENGINE_OPEN)
def open_game_engine():
    command = unreal_engine.get_unreal_editor_exe_path(utilities.get_unreal_engine_dir())
    utilities.run_app(command, ExecutionMode.ASYNC, utilities.get_engine_launch_args())
    thread_engine_monitor.engine_monitor_thread()


@hook_states.hook_state_decorator(HookStateType.POST_ENGINE_CLOSE)
def post_engine_closed_message():
    log.log_message(f'Closed Unreal Engine.')


@hook_states.hook_state_decorator(HookStateType.PRE_ENGINE_CLOSE)
def close_game_engine():
    if unreal_engine.get_win_dir_type(utilities.get_unreal_engine_dir()) == PackagingDirType.WINDOWS_NO_EDITOR:
        game_engine_processes = file_io.get_processes_by_substring('UE4Editor')
    else:
        game_engine_processes = file_io.get_processes_by_substring('UnrealEditor')
    for process_info in game_engine_processes:
        file_io.kill_process(process_info['name'])
    post_engine_closed_message()


def toggle_engine_off():
    close_game_engine()


def toggle_engine_on():
    open_game_engine()
