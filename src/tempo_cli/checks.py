import shutil
import subprocess


def check_git_is_installed() -> bool:
    from tempo_core import logger
    if shutil.which("git") is not None:
        logger.log_message("Git is installed.")
        return True
    else:
        logger.log_message("Git is NOT installed.")
        return False


def check_uv_is_installed() -> bool:
    from tempo_core import logger
    try:
        subprocess.run(
            ["uv", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        logger.log_message("uv is installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.log_message("uv is NOT installed.")
        return False
