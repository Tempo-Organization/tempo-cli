from pathlib import Path

import rich_click as click

from tempo_core import main_logic


@click.group()
def clean() -> None:
    """Clean related commands"""


command_help = "Cleans up the GitHub repository specified within the settings JSON."


@clean.command(name="full", help=command_help, short_help=command_help)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file",
)
def full(config_file: Path) -> None:
    main_logic.cleanup_full()


command_help = "Cleans up the directories made from cooking of the GitHub repository specified within the settings JSON."


@clean.command(name="cooked", help=command_help, short_help=command_help)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file",
)
def cooked(config_file: Path) -> None:
    main_logic.cleanup_cooked()


command_help = "Cleans up the directories made from building of the GitHub repository specified within the settings JSON."


@clean.command(name="build", help=command_help, short_help=command_help)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file",
)
def cleanup(config_file: Path) -> None:
    main_logic.cleanup_build()


command_help = """
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate a file list JSON, use the generate_file_list_json command.
"""


@clean.command(name="game", help=command_help, short_help=command_help)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file",
)
@click.option(
    "--output-json",
    type=click.Path(
        resolve_path=True,
        path_type=Path,
    ),
    help="Path to the output game file list json.",
)
def game(config_file: Path, output_json: Path) -> None:
    if output_json:
        main_logic.cleanup_game(output_json)
    else:
        main_logic.cleanup_game(None)



command_help = """
Cleans up the specified directory, deleting all files not specified within the file list JSON.
To generate one, use the generate_file_list command.
"""

@clean.command(name="from-file-list", help=command_help, short_help=command_help)
@click.argument(
    "file-list",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
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
        path_type=Path,
    ),
)
def from_file_list(file_list: Path, directory: Path) -> None:
    """
    Arguments:
        file_list (str): Path to the file list you want to clean from.
        directory (str): Path to the directory tree to clean up. It will delete all files not in the specified file list.
    """
    main_logic.cleanup_from_file_list(file_list, directory)



command_help = "Cleans up and resyncs a git project to the GitHub repository and branch specified within the settings JSON."


@clean.command(name="resync-dir-with-repo", help=command_help, short_help=command_help)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file",
)
def resync_dir_with_repo(config_file: Path) -> None:
    main_logic.resync_dir_with_repo()
