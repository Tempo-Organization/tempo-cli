import shutil
import subprocess


def check_git_is_installed() -> bool:
    if shutil.which("git") is not None:
        print("Git is installed.")
        return True
    else:
        print("Git is NOT installed.")
        return False


def check_uv_is_installed() -> bool:
    try:
        subprocess.run(
            ["uv", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        print("uv is installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("uv is NOT installed.")
        return False
