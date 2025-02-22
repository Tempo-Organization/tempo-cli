import os
import sys
import time

start_time = time.time()

from unreal_auto_mod import customization, file_io, log, log_info, main_logic


def initialization():
    if "--logs_directory" in sys.argv:
        index = sys.argv.index("--logs_directory") + 1
        if index < len(sys.argv):
            log_dir = f"{os.path.normpath(sys.argv[index].strip("'").strip('"'))}"
            log.set_log_base_dir(log_dir)
            log.configure_logging(log_info.LOG_INFO)
        else:
            log.set_log_base_dir(os.path.normpath(f'{file_io.SCRIPT_DIR}/logs'))
            log.configure_logging(log_info.LOG_INFO)
    else:
        try:
            log.set_log_base_dir(os.path.normpath(f'{file_io.SCRIPT_DIR}/logs'))
            log.configure_logging(log_info.LOG_INFO)
            customization.enable_vt100()
            main_logic.init_thread_system()
        except Exception as error_message:
            log.log_message(str(error_message))
