import os
import json
import pathlib
import subprocess
from dataclasses import dataclass, field

import tomlkit
import questionary
import rich_click as click

from tempo_core import logger
from tempo_core.main_logic import generate_uproject

from tempo_cli import file_io as tc_file_io
from tempo_cli import validators, checks, unreal, git
from tempo_cli.commitizen import data_structures as cz_data_structures


# DISABLED = True
# response = questionary.confirm("Are you amazed?").skip_if(DISABLED, default=True).ask()


# use Text to ask for free text input
# use Password to ask for free text where the text is hidden
# use File Path to ask for a file or directory path with autocompletion
# use Confirmation to ask a yes or no question
# use Select to ask the user to select one item from a beautiful list
# use Raw Select to ask the user to select one item from a list
# use Checkbox to ask the user to select any number of items from a list
# use Autocomplete to ask for free text with autocomplete help
# use Press Any Key To Continue to ask the user to press any key to continue


@dataclass
class SetupInformation:
    working_directory: pathlib.Path
    tempo_config: pathlib.Path | None = None
    tempo_config_contents: dict = field(default_factory=dict)
    git_repo_dir: pathlib.Path | None = None
    should_use_pre_commit: bool = False
    should_make_docs: bool = False
    should_download_easy_scripts: bool  = False
    should_use_versioning: bool  = False
    should_auto_close_game: bool  = False
    should_close_fmodel_and_umodel: bool  = False


def project_init(directory: pathlib.Path) -> None:
    # add initial select multi option thing ifg possible for features omn onitial step, using checkbox thing
    setup_information = SetupInformation(working_directory=directory)
    logger.log_message(f"project directory: {setup_information.working_directory}")
    setup_information.git_repo_dir = pathlib.Path(f"{setup_information.working_directory}/.git")
    setup_information.tempo_config = pathlib.Path(f"{setup_information.working_directory}/.tempo.json")
    if setup_information.tempo_config.exists() and setup_information.tempo_config.is_file():
        config_already_exists_error = (
            f'There is already a .tempo.json config in the following directory: "{setup_information.working_directory}"'
        )
        raise FileExistsError(config_already_exists_error)


    feature_choices = {
        "docs": "should_make_docs",
        "easy scripts": "should_download_easy_scripts",
        "version management": "should_use_versioning",
        "should auto close game": "should_auto_close_game",
        "should auto close fmodel and umodel": "should_close_fmodel_and_umodel",
        "should setup prek": "should_use_prek"
    }

    chosen_options = questionary.checkbox(
        message='Choose your features',
        choices=list(feature_choices.keys())
    ).ask()

    for option in chosen_options:
        setattr(setup_information, feature_choices[option], True)


    git_repo_dir_already_existed = False
    if os.path.isdir(setup_information.git_repo_dir):
        git_repo_dir_already_existed = True
        subprocess.run("git init")

    pyproject_toml = os.path.normpath(f"{setup_information.working_directory}/pyproject.toml")
    if not os.path.isfile(pyproject_toml):
        # subprocess.run("uv init --package", cwd=setup_information.working_directory)

        # Names must start and end with a letter or digit and may only contain -, _, ., and alphanumeric characters.
        # below might need validation for valid project names
        project_name = questionary.text(message='What would you like your project name to be?').ask()
        description = questionary.text(message='What would you like your project description to be?').ask()
        subprocess.run(f"uv init --bare --no-readme --no-pin-python --no-workspace --name {project_name} --description {description}", cwd=setup_information.working_directory)
    subprocess.run("uv add git+https://www.github.com/Tempo-Organization/tempo-cli", cwd=setup_information.working_directory)

    unreal_engine_dir = questionary.path(
        message='What is the path to your unreal engine install directory (Most mods will need this but not all)? Example: "C:/Program Files/Epic Games/UE_4.22" (press enter to skip)',
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
        setup_information.tempo_config_contents.setdefault("engine_info", {})["unreal_engine_dir"] = unreal_engine_dir
        version = unreal.get_unreal_engine_version(unreal_engine_dir)
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

    if "game_info" not in setup_information.tempo_config_contents:
        setup_information.tempo_config_contents["game_info"] = {}

    game_executable = ""
    if game_launch_choice == "exe":
        game_executable = questionary.path(
            message='What is the path to your main game executable? Example: "C:/Program Files (x86)/Steam/steamapps/common/Zedfest/KevinSpel/Binaries/Win64/Zedfest.exe" (press enter to skip)'
        ).ask()
        setup_information.tempo_config_contents["game_info"]["game_exe_path"] = game_executable
        setup_information.tempo_config_contents["game_info"]["launch_type"] = game_launch_choice
    if game_launch_choice == "steam":
        game_id = questionary.text(
            message="What is the steam game id for your game?",
            validate=validators.is_int_validator,
        ).ask()
        setup_information.tempo_config_contents["game_info"]["game_id"] = game_id
        setup_information.tempo_config_contents["game_info"]["launch_type"] = game_launch_choice


    if "git_info" not in setup_information.tempo_config_contents:
        setup_information.tempo_config_contents["git_info"] = {}

    if git_repo_dir_already_existed:
        setup_information.tempo_config_contents["git_info"]["repo_branch"] = git.get_branch_from_git_repo(str(setup_information.git_repo_dir))
    else:
        gitignore = os.path.normpath(f"{setup_information.working_directory}/.gitignore")
        if os.path.isfile(gitignore):
            os.remove(gitignore)
        tc_file_io.download_files_from_github_repo(
            repo_url="https://github.com/Tempo-Organization/tempo-template",
            repo_branch="main",
            file_paths=[".gitignore"],
            output_directory=str(setup_information.working_directory),
        )
        setup_information.tempo_config_contents["git_info"]["repo_branch"] = "master"
    setup_information.tempo_config_contents["git_info"]["repo_path"] = setup_information.working_directory

    if setup_information.should_make_docs:
        documentation_setup(setup_information)

    if setup_information.should_use_pre_commit:
        pre_commit_setup(setup_information)

    if setup_information.should_use_versioning:
        versioning_setup(setup_information)

    uproject_path = questionary.path(
        message='What is the path to your uproject, if you have one already? Example: "C:/Users/Mythi/Documents/GitHub/ZedfestModdingKit/KevinSpel.uproject" (press enter to skip)',
    ).ask()
    if not uproject_path == "" and not os.path.dirname(uproject_path) == setup_information.working_directory:
        logger.log_message(
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
            project_file=os.path.normpath(f"{setup_information.working_directory}/{uproject_name}.uproject"),
            file_version=3,
            engine_major_association=unreal_engine_major_version,
            engine_minor_association=unreal_engine_minor_version,
            ignore_safety_checks=True,
        )
        setup_information.tempo_config_contents['engine_info']['unreal_project_file'] = os.path.normpath(f"{setup_information.working_directory}/{uproject_name}.uproject")
    else:
        if not uproject_path == "" and uproject_path:
            setup_information.tempo_config_contents['engine_info']['unreal_project_file'] = uproject_path

    window_override_title = questionary.text(
        message='What is title of the game window, when the game is launched? Example: "Zedfest" (press enter to skip)'
    ).ask()
    if not window_override_title == "" and window_override_title:
        setup_information.tempo_config_contents["game_info"]["window_title_override"] = window_override_title

    setup_information.tempo_config_contents.setdefault("process_kill_events", {})

    if setup_information.should_close_fmodel_and_umodel:
        setup_information.tempo_config_contents["process_kill_events"]["processes"] = [
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

    if setup_information.should_auto_close_game:
        setup_information.tempo_config_contents["process_kill_events"]["auto_close_game"] = True

    if setup_information.should_download_easy_scripts:
        easy_scripts_setup(setup_information)

    def convert_paths(obj): # noqa
        if isinstance(obj, pathlib.Path):
            return str(obj)
        elif isinstance(obj, dict):
            return {k: convert_paths(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_paths(v) for v in obj]
        else:
            return obj

    cleaned_data = convert_paths(setup_information.tempo_config_contents)

    with open(setup_information.tempo_config, "w") as config_file:
        json.dump(cleaned_data, config_file, indent=4)

    logger.log_message(f'.tempo.json created at "{setup_information.tempo_config}".')


@click.command(
    name="init",
    help="Create a new tempo project.",
    short_help="Create a new tempo project",
)
@click.option(
    "--directory",
    default=os.getcwd(),
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path, file_okay=False, dir_okay=True),
    help="The tempo project directory, defaults to current working directory.",
)
# add game preset options later?
def init(directory: pathlib.Path) -> None:
    if not checks.check_git_is_installed():
        no_git_error = 'You need git installed to use this functionality.'
        raise RuntimeError(no_git_error)

    if not checks.check_uv_is_installed():
        no_uv_error = 'You need uv installed to use this functionality.'
        raise RuntimeError(no_uv_error)

    project_init(directory)


def pre_commit_setup(setup_information: SetupInformation) -> None:
    tc_file_io.download_files_from_github_repo(
        repo_url="https://github.com/Tempo-Organization/tempo-template",
        repo_branch="main",
        file_paths=[".pre-commit-config.yaml"],
        output_directory=str(setup_information.working_directory),
    )
    subprocess.run("uv add prek")
    subprocess.run("uv run prek install")


def versioning_setup(setup_information: SetupInformation) -> None:
    subprocess.run("uv add commitizen")
    toml_path = os.path.normpath(f"{setup_information.working_directory}/pyproject.toml")
    with open(toml_path, "r", encoding="utf-8") as f:
        content = f.read()
        toml_doc = tomlkit.parse(content)

    version_scheme_options = cz_data_structures.get_enum_strings_from_enum(cz_data_structures.CommitizenVersionSchemeOption)
    version_scheme_option = questionary.select(
        message="Which versioning scheme would you like to use?",
        choices=version_scheme_options,
        default=cz_data_structures.CommitizenVersionSchemeOption.SEMVER2.value
    ).ask()
    commitizen_table = tomlkit.table()
    commitizen_table["name"] = "cz_conventional_commits"
    commitizen_table["tag_format"] = "$version"
    commitizen_table["version_scheme"] = version_scheme_option
    commitizen_table["version_provider"] = "commitizen"
    commitizen_table["version"] = "0.1.0"
    commitizen_table["update_changelog_on_bump"] = True

    if "tool" not in toml_doc:
        toml_doc["tool"] = tomlkit.table()

    toml_doc["tool"]["commitizen"] = commitizen_table  # type: ignore

    with open(toml_path, "w", encoding="utf-8") as f:
        f.write(tomlkit.dumps(toml_doc))

    if setup_information.should_use_pre_commit:
        subprocess.run("uv run prek install --hook-type commit-msg")
        subprocess.run("uv run prek install --hook-type pre-push")


def process_management_setup() -> None:
    return


def easy_scripts_setup(setup_information: SetupInformation) -> None:
    if not setup_information.tempo_config:
        raise FileNotFoundError(setup_information.tempo_config)
    EASY_SCRIPTS_VERSION = "0.4.0"
    output_directory_for_scripts = os.path.join(setup_information.working_directory, "Modding", "scripts")

    easy_scripts_download_link = (
        f"https://github.com/Tempo-Organization/tempo-template/"
        f"releases/download/{EASY_SCRIPTS_VERSION}/easy_scripts.zip"
    )

    tc_file_io.download_and_extract_zip(
        url=easy_scripts_download_link,
        output_dir=output_directory_for_scripts
    )


def documentation_setup(setup_information: SetupInformation) -> None:
    subprocess.run("uv add mkdocs-material")
    files = [
        "mkdocs.yml",
        ".github/workflows/github_pages.yml",
        "docs/index.md",
        "docs/stylesheets/extra.css",
    ]
    tc_file_io.download_files_from_github_repo(
        repo_url="https://github.com/Tempo-Organization/tempo-template",
        repo_branch="main",
        file_paths=files,
        output_directory=str(setup_information.working_directory),
    )
    mkdocs_yml_path = os.path.normpath(f'{setup_information.working_directory}/mkdocs.yml')
    index_md_path = os.path.normpath(f'{setup_information.working_directory}/docs/index.md')
    mod_name = questionary.text(message="What is the main name for your docs? Usually your main Mod Name.").ask()
    github_account_name = questionary.text(message="What is your github account name?").ask()
    discord_server_link = questionary.text(message="If you have one, what is your discord server link? If none leave blank and hit enter.").ask()
    if discord_server_link == '':
        discord_server_link = 'https://discord.gg/EvUuAD4QvS'
    tc_file_io.replace_text_in_file(index_md_path, "ModName", mod_name)
    tc_file_io.replace_text_in_file(mkdocs_yml_path, "ModName", mod_name)
    tc_file_io.replace_text_in_file(mkdocs_yml_path, "GithubAccount", github_account_name)
    tc_file_io.replace_text_in_file(mkdocs_yml_path, "logo: fontawesome/solid/?", f'logo: fontawesome/solid/{mod_name[0]}')
    tc_file_io.replace_text_in_file(mkdocs_yml_path, "Your Discord Here", discord_server_link)
