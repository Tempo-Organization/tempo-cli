import time
import threading

from unreal_auto_mod import hook_states, unreal_engine, utilities, window_management, log, processes
from unreal_auto_mod.data_structures import HookStateType

init_done = False


def engine_monitor_thread():
    # later on have this only activate when
    start_engine_monitor_thread()
    log.log_message('Thread: Engine Monitoring Thread Started')
    engine_monitor_thread.join()
    log.log_message('Thread: Engine Monitoring Thread Ended')


def engine_monitor_thread_runner(tick_rate: float = 0.01):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        engine_monitor_thread_logic()


@hook_states.hook_state_decorator(HookStateType.POST_ENGINE_OPEN)
def found_engine_window():
    global found_window
    log.log_message('Window: Engine Window Found')
    found_window = True


def engine_monitor_thread_logic():
    global found_process
    global found_window
    global window_closed
    global init_done

    if not init_done:
        found_process = False
        found_window = False
        window_closed = False
        init_done = True

    engine_window_name = unreal_engine.get_engine_window_title(utilities.get_uproject_file())
    if not found_process:
        engine_process_name = unreal_engine.get_engine_process_name(utilities.get_unreal_engine_dir())
        if processes.is_process_running(engine_process_name):
            log.log_message('Process: Found Engine Process')
            found_process = True
    elif not found_window:
        if window_management.does_window_exist(engine_window_name):
            found_engine_window()
    elif not window_closed:
        if not window_management.does_window_exist(engine_window_name):
            log.log_message('Window: Engine Window Closed')
            window_closed = True
            stop_engine_monitor_thread()


def start_engine_monitor_thread():
    global engine_monitor_thread
    global run_monitoring_thread
    run_monitoring_thread = True
    engine_monitor_thread = threading.Thread(target=engine_monitor_thread_runner, daemon=True)
    engine_monitor_thread.start()


@hook_states.hook_state_decorator(HookStateType.POST_ENGINE_CLOSE)
def stop_engine_monitor_thread():
    global run_monitoring_thread
    run_monitoring_thread = False
