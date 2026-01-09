import pathlib

import rich_click as click

from tempo_core import main_logic


@click.group()
def clean():
    """Clean related commands"""
    click.echo("Starting clean command usage...")


command_help = "Cleans up the GitHub repository specified within the settings JSON."


@clean.command(name="full", help=command_help, short_help=command_help)
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
def full(settings_json):
    main_logic.cleanup_full()


command_help = "Cleans up the directories made from cooking of the GitHub repository specified within the settings JSON."


@clean.command(name="cooked", help=command_help, short_help=command_help)
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
def cooked(settings_json):
    main_logic.cleanup_cooked()


command_help = "Cleans up the directories made from building of the GitHub repository specified within the settings JSON."


@clean.command(name="build", help=command_help, short_help=command_help)
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
def cleanup(settings_json):
    main_logic.cleanup_build()


command_help = """
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate a file list JSON, use the generate_file_list_json command.
"""


@clean.command(name="game", help=command_help, short_help=command_help)
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
def game(settings_json, output_json):
    if output_json:
        main_logic.cleanup_game(output_json)
    else:
        main_logic.cleanup_game(None)



command_help = """
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate one, use the generate_file_list command.
"""

@clean.command(name="from_file_list", help=command_help, short_help=command_help)
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
def from_file_list(file_list, directory):
    """
    Arguments:
        file_list (str): Path to the file list you want to clean from.
        directory (str): Path to the directory tree to clean up. It will delete all files not in the specified file list.
    """
    main_logic.cleanup_from_file_list(file_list, directory)



command_help = "Cleans up and resyncs a git project to the GitHub repository and branch specified within the settings JSON."


@clean.command(name="resync_dir_with_repo", help=command_help, short_help=command_help)
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
def resync_dir_with_repo(settings_json):
    main_logic.resync_dir_with_repo()
