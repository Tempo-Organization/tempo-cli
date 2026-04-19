import os
import pathlib

import rich_click as click

from tempo_core import main_logic
from tempo_core import file_io as tempo_core_file_io


@click.group()
def file_io() -> None:
    """File IO related commands"""


command_help = "Zip Directory Tree"

@file_io.command(name="zip", help=command_help, short_help=command_help)
@click.option(
    "--directory",
    help="Path to the directory tree whose content to zip.",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    required=True,
)
@click.option(
    "--zip",
    help="Path to the output zip file.",
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    required=True,
)
def zip_directory_tree(directory: pathlib.Path, zip: pathlib.Path) -> None:
    tempo_core_file_io.zip_directory_tree(
        input_dir=str(directory),
        output_dir=os.path.dirname(zip),
        zip_name=os.path.basename(zip),
    )


command_help = "Unzip"


@file_io.command(name="unzip", help=command_help, short_help=command_help)
@click.option(
    "--output_directory",
    help="Path to the directory to unzip the zip to.",
    type=click.Path(
        file_okay=False, dir_okay=True, resolve_path=True, path_type=pathlib.Path
    ),
    required=True,
)
@click.option(
    "--zip",
    help="Path to the zip.",
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    required=True,
)
def unzip(output_directory: pathlib.Path, input_zip: pathlib.Path) -> None:
    tempo_core_file_io.unzip_zip(zip_path=str(input_zip), output_location=str(output_directory))


command_help = "Move a file or directory to a new location."


@file_io.command(name="move", help=command_help, short_help=command_help)
@click.option(
    "--input_path",
    help="The input path, to a directory tree or file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--output_path",
    help="The output path, to a directory tree or file.",
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--overwrite", is_flag=True, help="Overwrite existing files if they already exist."
)
def move(input_path: pathlib.Path, output_path: pathlib.Path, overwrite: bool) -> None:
    tempo_core_file_io.move(input_path, output_path, overwrite)


command_help = "Copy a file or directory to a new location."


@file_io.command(name="copy", help=command_help, short_help=command_help)
@click.option(
    "--input_path",
    help="The input path, to a directory tree or file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--output_path",
    help="The output path, to a directory tree or file.",
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--overwrite", is_flag=True, help="Overwrite existing files if they already exist."
)
def copy(input_path: pathlib.Path, output_path: pathlib.Path, overwrite: bool) -> None:
    tempo_core_file_io.copy(input_path, output_path, overwrite=overwrite)


command_help = "Symlink a file or directory to a new location."


@file_io.command(name="symlink", help=command_help, short_help=command_help)
@click.option(
    "--input_path",
    help="The input path, to a directory tree or file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--output_path",
    help="The output path, to a directory tree or file.",
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--overwrite",
    is_flag=True,
    help="Overwrite existing files if they already exist.",
)
def symlink(input_path: pathlib.Path, output_path: pathlib.Path, overwrite: bool) -> None:
    tempo_core_file_io.symlink(input_path, output_path, overwrite)


command_help = "Delete one or more files and/or directories."


@file_io.command(name="delete", help=command_help, short_help=command_help)
@click.option(
    "--input_paths",
    help="The input path, to a directory tree or file to delete, can be specified multiple times.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
    multiple=True,
)
def delete(input_paths: list[pathlib.Path]) -> None:
    tempo_core_file_io.delete(input_paths)



command_help = "Opens the latest log file."


@file_io.command(name="open_latest_log", help=command_help, short_help=command_help)
@click.option(
    "--settings_json",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
def open_latest_log(settings_json: pathlib.Path) -> None:
    main_logic.open_latest_log()

command_help = "Generates a JSON file containing all of the files in the game directory, from the game exe specified within the settings JSON."


@file_io.command(
    name="generate_game_file_list_json", help=command_help, short_help=command_help
)
@click.option(
    "--settings_json",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    required=True,
    help="Path to the settings JSON file",
)
@click.option(
    "--output_json",
    type=click.Path(
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="Path to the output game file list json."
)
def generate_game_file_list_json(settings_json: pathlib.Path, output_json: pathlib.Path) -> None:
    if output_json:
        main_logic.generate_game_file_list_json(output_json)
    else:
        main_logic.generate_game_file_list_json(None)



command_help = (
    "Generates a JSON file containing all of the files in the specified directory."
)

@file_io.command(name="generate_file_list", help=command_help, short_help=command_help)
@click.argument(
    "directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.argument(
    "file_list",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
def generate_file_list(directory: pathlib.Path, file_list: list[pathlib.Path]) -> None:
    """
    Arguments:
        directory (str): Path to the directory tree you want to generate the file list from.
        file_list (str): Path to the output file, saved in JSON format.
    """
    main_logic.generate_file_list(str(directory), str(file_list))
