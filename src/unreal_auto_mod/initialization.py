import time

start_time = time.time()

from unreal_auto_mod import log, log_info, file_io, customization, main_logic


def initialization():
    try:
        log.set_log_base_dir(file_io.SCRIPT_DIR)
        log.configure_logging(log_info.LOG_INFO)
        customization.enable_vt100()
        main_logic.init_thread_system()
    except Exception as error_message:
        log.log_message(str(error_message))
