import os


def file_exists_validator(path: str):
    if not path:
        return "Path cannot be empty."

    # Strip quotes and whitespace
    path = path.strip().strip('"').strip("'")
    norm_path = os.path.normpath(path)

    if not os.path.isfile(norm_path):
        return f"File does not exist: {norm_path}"

    return True


def dir_exists_validator(path: str):
    if not path:
        return "Path cannot be empty."

    # Strip quotes and whitespace
    path = path.strip().strip('"').strip("'")
    norm_path = os.path.normpath(path)

    if not os.path.isdir(norm_path):
        return f"Directory does not exist: {norm_path}"

    return True


def exe_exists_validator(path: str):
    if not path:
        return "Path cannot be empty."

    # Strip quotes and whitespace
    path = path.strip().strip('"').strip("'")
    norm_path = os.path.normpath(path)

    if not os.path.isfile(norm_path):
        return f"File does not exist: {norm_path}"

    if not norm_path.lower().endswith(".exe"):
        return f"File is not an executable (.exe): {norm_path}"

    return True


def is_int_validator(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
