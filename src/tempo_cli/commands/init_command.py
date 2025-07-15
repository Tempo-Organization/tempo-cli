import os
import json
import subprocess

import tomlkit
import requests
import questionary
from tempo_core.main_logic import generate_uproject
from tempo_core import file_io

from tempo_cli import validators


def get_unreal_engine_version(engine_path: str) -> str:
    version_file_path = f"{engine_path}/Engine/Build/Build.version"
    file_io.check_path_exists(version_file_path)
    with open(version_file_path) as f:
        version_info = json.load(f)
        unreal_engine_major_version = version_info.get("MajorVersion", 0)
        unreal_engine_minor_version = version_info.get("MinorVersion", 0)
        return f"{unreal_engine_major_version}.{unreal_engine_minor_version}"


def download_files_from_github_repo(
    repo_url: str,
    repo_branch: str = "master",
    file_paths: list[str] = [],
    output_directory: str = os.getcwd(),
):
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
            print(f"Failed to download {file_path}: {e}")
            continue

        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        with open(local_file_path, "wb") as f:
            f.write(response.content)
            print(f"Downloaded: {file_path} → {local_file_path}")


def deep_update(original, updates):
    for key, value in updates.items():
        if key == "processes":
            # Ensure both original and value are lists of dicts
            if not isinstance(original.get(key), list):
                # If original is a dict or None, convert to list
                if isinstance(original.get(key), dict):
                    original[key] = [original[key]]
                else:
                    original[key] = []
            if isinstance(value, dict):
                value = [value]
            if isinstance(value, list):
                original[key].extend(value)
            else:
                # fallback: just replace
                original[key] = value
        elif isinstance(value, dict) and isinstance(original.get(key), dict):
            deep_update(original[key], value)
        else:
            original[key] = value


# will return HEAD for repos not on github yet, because detached, so assume we created with default
def get_branch_from_git_repo(repo_directory: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", repo_directory, "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        if result.stdout.strip() == "HEAD":
            return "master"
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def basic_init():
    cwd = os.getcwd()
    git_repo_dir = os.path.normpath(f"{cwd}/.git")
    print(f"current directory: {cwd}")
    tempo_config = os.path.normpath(f"{cwd}/.tempo.json")
    if os.path.isfile(tempo_config):
        config_already_exists_error = (
            f'There is already a .tempo.json config in the following directory: "{cwd}"'
        )
        raise FileExistsError(config_already_exists_error)

    tempo_json = {}

    if os.path.isdir(git_repo_dir):
        git_repo_dir_already_existed = True
    else:
        git_repo_dir_already_existed = False
    subprocess.run("uv init", cwd=cwd)

    main_py_file = os.path.normpath(f"{cwd}/main.py")
    if os.path.isfile(main_py_file):
        os.remove(main_py_file)

    unreal_engine_dir = questionary.path(
        message='What is the path to your unreal engine install directory? Example: "C:/Program Files/Epic Games/UE_4.22" (press enter to skip)',
        only_directories=True,
    ).ask()

    if unreal_engine_dir == "" or not unreal_engine_dir:
        unreal_engine_major_version = questionary.text(
            message='What is the unreal engine major version for this game? Example: "4" from 4.27 or 4.27.x, or "5" from 5.1 or 5.1.x',
            validate=validators.is_int_validator,
        ).ask()
        unreal_engine_minor_version = questionary.text(
            message='What is the unreal engine minor version for this game? Example: "27" from 4.27 or 4.27.x, or "1" from 5.1 or 5.1.x',
            validate=validators.is_int_validator,
        ).ask()
    else:
        deep_update(
            tempo_json, {"engine_info": {"unreal_engine_dir": unreal_engine_dir}}
        )
        version = get_unreal_engine_version(unreal_engine_dir)
        major, minor = version.split(".")
        unreal_engine_major_version = int(major)
        unreal_engine_minor_version = int(minor)

    game_launch_choice_options = [
        questionary.Choice("Exe", "exe"),
        questionary.Choice("Steam", "steam"),
        questionary.Choice("None", "None"),
    ]
    game_launch_choice = questionary.select(
        message="Would you like to launch the game through exe, steam, or not provide game launch options?",
        choices=game_launch_choice_options,
    ).ask()

    game_executable = ""
    if game_launch_choice == "exe":
        game_executable = questionary.path(
            message='What is the path to your main game executable? Example: "C:/Program Files (x86)/Steam/steamapps/common/Zedfest/KevinSpel/Binaries/Win64/Zedfest.exe" (press enter to skip)'
        ).ask()
        deep_update(tempo_json, {"game_info": {"game_exe_path": game_executable}})
        deep_update(tempo_json, {"game_info": {"launch_type": game_launch_choice}})
    if game_launch_choice == "steam":
        game_id = questionary.text(
            message="What is the steam game id for your game?",
            validate=validators.is_int_validator,
        ).ask()
        deep_update(tempo_json, {"game_info": {"game_id": game_id}})
        deep_update(tempo_json, {"game_info": {"launch_type": game_launch_choice}})

    if git_repo_dir_already_existed:
        deep_update(
            tempo_json,
            {"git_info": {"repo_branch": get_branch_from_git_repo(git_repo_dir)}},
        )
    else:
        gitignore = os.path.normpath(f"{os.getcwd()}/.gitignore")
        os.remove(gitignore)
        download_files_from_github_repo(
            repo_url="https://github.com/Tempo-Organization/tempo-template",
            repo_branch="main",
            file_paths=[".gitignore"],
            output_directory=cwd,
        )
        deep_update(tempo_json, {"git_info": {"repo_branch": "master"}})
    deep_update(tempo_json, {"git_info": {"repo_path": cwd}})

    should_make_docs = questionary.confirm(
        message="Would you like have tempo setup documentation for your project?",
        default=True,
    ).ask()
    if should_make_docs:
        subprocess.run("uv add mkdocs-material")
        files = [
            "mkdocs.yml",
            ".github/workflows/github_pages.yml",
            "docs/index.md",
            "docs/stylesheets/extra.css",
        ]
        download_files_from_github_repo(
            repo_url="https://github.com/Tempo-Organization/tempo-template",
            repo_branch="main",
            file_paths=files,
            output_directory=cwd,
        )

    should_use_pre_commit = questionary.confirm(
        message="Would you like have tempo setup pre-commit for various features?",
        default=True,
    ).ask()
    if should_use_pre_commit:
        download_files_from_github_repo(
            repo_url="https://github.com/Tempo-Organization/tempo-template",
            repo_branch="main",
            file_paths=[".pre-commit-config.yaml"],
            output_directory=cwd,
        )
        subprocess.run("uv add pre-commit")
        subprocess.run("uv run pre-commit install")

    should_use_versioning = questionary.confirm(
        message="Would you like have tempo setup versioning management for your project?",
        default=True,
    ).ask()
    if should_use_versioning:
        subprocess.run("uv add commitizen")
        toml_path = os.path.normpath(f"{cwd}/pyproject.toml")
        with open(toml_path, "r", encoding="utf-8") as f:
            content = f.read()
            toml_doc = tomlkit.parse(content)

        commitizen_table = tomlkit.table()
        commitizen_table["name"] = "cz_conventional_commits"
        commitizen_table["tag_format"] = "$version"
        commitizen_table["version_scheme"] = "semver2"
        commitizen_table["version_provider"] = "uv"
        commitizen_table["update_changelog_on_bump"] = True

        if "tool" not in toml_doc:
            toml_doc["tool"] = tomlkit.table()

        toml_doc["tool"]["commitizen"] = commitizen_table  # type: ignore

        with open(toml_path, "w", encoding="utf-8") as f:
            f.write(tomlkit.dumps(toml_doc))

        if should_use_pre_commit:
            subprocess.run("uv run pre-commit install --hook-type commit-msg")
            subprocess.run("uv run pre-commit install --hook-type pre-push")

    uproject_path = questionary.path(
        message='What is the path to your uproject, if you have one already? Example: "C:/Users/Mythi/Documents/GitHub/ZedfestModdingKit/KevinSpel.uproject" (press enter to skip)',
    ).ask()
    if not uproject_path == "" and not os.path.dirname(uproject_path) == os.getcwd():
        print(
            "Warning: It is recommended to place your uproject in the same directory as your tempo project files."
        )
    if uproject_path == "" or not uproject_path:
        if not game_executable or game_executable == "":
            uproject_name = questionary.text(
                message="What is the name of your uproject file? (it should be the same as the game project name usually.)"
            ).ask()
        else:
            uproject_name = uproject_name = os.path.basename(
                os.path.dirname(os.path.dirname(os.path.dirname(game_executable)))
            )
        generate_uproject(
            project_file=os.path.normpath(f"{cwd}/{uproject_name}.uproject"),
            file_version=3,
            engine_major_association=unreal_engine_major_version,
            engine_minor_association=unreal_engine_minor_version,
            ignore_safety_checks=True,
        )

    window_override_title = questionary.text(
        message='What is title of the game window, when the game is launched? Example: "Zedfest" (press enter to skip)'
    ).ask()
    if not window_override_title == "" and window_override_title:
        deep_update(
            tempo_json, {"general_info": {"window_title": window_override_title}}
        )

    should_close_fmodel_and_umodel = questionary.confirm(
        message="Would you like to automatically close any open fmodel and umodel instances as need be?",
        default=True,
    ).ask()
    if should_close_fmodel_and_umodel:
        deep_update(
            tempo_json,
            {
                "process_kill_events": {
                    "processes": [
                        {
                            "hook_state": "constant",
                            "process_name": "Fmodel",
                            "use_substring_check": True,
                        },
                        {
                            "hook_state": "constant",
                            "process_name": "Umodel",
                            "use_substring_check": True,
                        },
                    ]
                }
            },
        )
    should_auto_close_game = questionary.confirm(
        message="Would you like to automatically close the game as need be?",
        default=True,
    ).ask()
    if should_auto_close_game:
        deep_update(
            tempo_json,
            {"process_kill_events": {"auto_close_game": should_auto_close_game}},
        )

    # print()

    # print('tempo json contents:')
    # print(tempo_json)

    # print()

    with open(tempo_config, "w") as config_file:
        json.dump(tempo_json, config_file, indent=4)

    print(f'.tempo.json created at "{tempo_config}".')


def advanced_init():
    print("Currently not implemented.")
