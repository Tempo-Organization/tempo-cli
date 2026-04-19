import os
import zipfile
import requests

from tempo_core import logger


def download_and_extract_zip(url: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    zip_path = os.path.join(output_dir, "easy_scripts.zip")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    os.remove(zip_path)


def replace_text_in_file(file_path: str, old_text: str, new_text: str) -> None:
    """
    Reads a file, replaces all occurrences of old_text with new_text,
    and writes the changes back to the file.
    """
    with open(file_path, 'r') as file:
        file_data = file.read()

    file_data = file_data.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(file_data)

    logger.log_message(f"Text replacement completed successfully in {file_path}")


def download_files_from_github_repo(
    repo_url: str,
    repo_branch: str = "master",
    file_paths: list[str] = [],
    output_directory: str = os.getcwd(),
) -> None:
    try:
        parts = repo_url.strip("/").split("/")
        user, repo = parts[-2], parts[-1]
    except IndexError:
        raise ValueError("Invalid GitHub repository URL")

    for file_path in file_paths:
        raw_url = (
            f"https://raw.githubusercontent.com/{user}/{repo}/{repo_branch}/{file_path}"
        )
        local_file_path = os.path.join(output_directory, file_path)

        try:
            response = requests.get(raw_url)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.log_message(f"Failed to download {file_path}: {e}")
            continue

        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        with open(local_file_path, "wb") as f:
            f.write(response.content)
            logger.log_message(f"Downloaded: {file_path} to {local_file_path}")


# def deep_update(original, updates):
#     for key, value in updates.items():
#         if key == "processes":
#             # Ensure both original and value are lists of dicts
#             if not isinstance(original.get(key), list):
#                 # If original is a dict or None, convert to list
#                 if isinstance(original.get(key), dict):
#                     original[key] = [original[key]]
#                 else:
#                     original[key] = []
#             if isinstance(value, dict):
#                 value = [value]
#             if isinstance(value, list):
#                 original[key].extend(value)
#             else:
#                 # fallback: just replace
#                 original[key] = value
#         elif isinstance(value, dict) and isinstance(original.get(key), dict):
#             deep_update(original[key], value)
#         else:
#             original[key] = value
