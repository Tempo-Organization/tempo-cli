import os
import sys

from unreal_auto_mod import (
    customization, 
    file_io, 
    log_info, 
    logger, 
    main_logic,
    window_management,
    wrapper,
    settings
)
from unreal_auto_mod.programs import repak


def initialization():
    window_management.change_window_name('unreal_auto_mod')
    if "--logs_directory" in sys.argv:
        index = sys.argv.index("--logs_directory") + 1
        if index < len(sys.argv):
            log_dir = f"{os.path.normpath(sys.argv[index].strip("'").strip('"'))}"
            logger.set_log_base_dir(log_dir)
            logger.configure_logging(log_info.LOG_INFO)
        else:
            logger.set_log_base_dir(os.path.normpath(f'{file_io.SCRIPT_DIR}/logs'))
            logger.configure_logging(log_info.LOG_INFO)
    else:
        try:
            logger.set_log_base_dir(os.path.normpath(f'{file_io.SCRIPT_DIR}/logs'))
            logger.configure_logging(log_info.LOG_INFO)
            customization.enable_vt100()
            main_logic.init_thread_system()
        except Exception as error_message:
            logger.log_message(str(error_message))
    check_generate_wrapper()
    check_settings()
    


def check_generate_wrapper():
    if "--generate_wrapper" in sys.argv:
        wrapper.generate_wrapper()


def check_settings():
    try:
        if "--settings_json" in sys.argv:
            index = sys.argv.index("--settings_json") + 1
            if index < len(sys.argv):
                settings_file = f"{os.path.normpath(sys.argv[index].strip("'").strip('"'))}"
                settings_to_return = settings.load_settings(settings_file)
                repak.ensure_repak_installed()
                return settings_to_return
            else:
                print("Error: No file path provided after --settings_json.")
                sys.exit(1)
    except Exception as e:
        print(f"Error processing settings: {e}")
        sys.exit(1)
