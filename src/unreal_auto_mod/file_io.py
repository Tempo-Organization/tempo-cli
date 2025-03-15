import glob
import hashlib
import os
import sys
import webbrowser
import zipfile
from pathlib import Path

import psutil
import requests
from requests.exceptions import HTTPError, RequestException

from unreal_auto_mod.logger import log_message

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).resolve().parent


def unzip_zip(zip_path: str, output_location: str):
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_location)


def download_file(url: str, download_path: str):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        os.makedirs(os.path.dirname(download_path), exist_ok=True)

        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        log_message(f"Download completed: {download_path}")

    except HTTPError as http_err:
        log_message(f"HTTP error occurred while downloading {url}: {http_err}")
    except RequestException as req_err:
        log_message(f"Request error occurred while downloading {url}: {req_err}")
    except OSError as io_err:
        log_message(f"File I/O error occurred while saving to {download_path}: {io_err}")
    except Exception as err:
        log_message(f"An unexpected error occurred: {err}")


def open_dir_in_file_browser(input_directory: str):
    formatted_directory = os.path.abspath(input_directory)
    if not os.path.isdir(formatted_directory):
        log_message(f"Error: The directory '{formatted_directory}' does not exist.")
        return
    os.startfile(formatted_directory)


def open_file_in_default(file_path: str):
    os.startfile(file_path)


def open_website(input_url: str):
    webbrowser.open(input_url)


def check_directory_exists(dir_path: str) -> bool:
    if os.path.isdir(dir_path):
        return True
    else:
        raise NotADirectoryError(f'Check: "{dir_path}" directory not found.')


def check_path_exists(path: str) -> bool:
    if os.path.exists(path):
        return True
    else:
        raise FileNotFoundError(f'Check: "{path}" path is not a directory or file.')


def check_file_exists(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        raise FileNotFoundError(f'Check: "{file_path}" file not found.')


def kill_process(process_name: str):
    os.system(f'taskkill /f /im "{process_name}"')


def get_processes_by_substring(substring: str) -> list:
    all_processes = psutil.process_iter(['pid', 'name'])
    matching_processes = [proc.info for proc in all_processes if substring.lower() in proc.info['name'].lower()]
    return matching_processes


def get_file_hash(file_path: str) -> str:
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
    return md5.hexdigest()


def get_do_files_have_same_hash(file_path_one: str, file_path_two: str) -> bool:
    if os.path.exists(file_path_one) and os.path.exists(file_path_two):
        return get_file_hash(file_path_one) == get_file_hash(file_path_two)
    else:
        return False


def get_files_in_tree(tree_path: str) -> list:
    return glob.glob(tree_path + '/**/*', recursive=True)


def get_file_extension(file_path: str) -> str:
    _, file_extension = os.path.splitext(file_path)
    return file_extension


# returns .extension not extension
def get_file_extensions(file_path: str) -> list:
    directory = os.path.dirname(file_path)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    extensions = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_base_name, ext = os.path.splitext(file)
            if file_base_name == base_name and ext:
                extensions.add(ext)
    return sorted(extensions)


# returns extension, not .extension
def get_file_extensions_two(directory_with_base_name: str) -> list:
    directory, base_name = os.path.split(directory_with_base_name)
    extensions = set()
    for _, files in os.walk(directory):
        for file in files:
            if file.startswith(base_name):
                _, ext = os.path.splitext(file)
                if ext:
                    extensions.add(ext)
    return list(extensions)


def get_files_in_dir(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def filter_by_extension(files, extension):
    return [f for f in files if f.lower().endswith(extension)]


def get_all_lines_in_config(config_path: str) -> list[str]:
    with open(config_path, encoding='utf-8') as file:
        return file.readlines()


def set_all_lines_in_config(config_path: str, lines: list[str]):
    with open(config_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def add_line_to_config(config_path: str, line: str):
    if not does_config_have_line(config_path, line):
        with open(config_path, 'a', encoding='utf-8') as file:
            file.write(line + '\n')


def remove_line_from_config(config_path: str, line: str):
    lines = get_all_lines_in_config(config_path)
    with open(config_path, 'w', encoding='utf-8') as file:
        file.writelines(l for l in lines if l.rstrip('\n') != line)


def does_config_have_line(config_path: str, line: str) -> bool:
    return line + '\n' in get_all_lines_in_config(config_path)


def remove_lines_from_config_that_start_with_substring(config_path: str, substring: str):
    new_lines = []
    for line in get_all_lines_in_config(config_path):
        if not line.startswith(substring):
            new_lines.append(line)
    set_all_lines_in_config(config_path, new_lines)


def remove_lines_from_config_that_end_with_substring(config_path: str, substring: str):
    new_lines = []
    for line in get_all_lines_in_config(config_path):
        if not line.endswith(substring):
            new_lines.append(line)
    set_all_lines_in_config(config_path, new_lines)


def remove_lines_from_config_that_contain_substring(config_path: str, substring: str):
    new_lines = []
    for line in get_all_lines_in_config(config_path):
        if line not in (substring):
            new_lines.append(line)
    set_all_lines_in_config(config_path, new_lines)


def get_platform_wrapper_extension() -> str:
    return "bat" if os.name == "nt" else "sh"


def ensure_path_quoted(path: str) -> str:
    return f'"{path}"' if not path.startswith('"') and not path.endswith('"') else path
