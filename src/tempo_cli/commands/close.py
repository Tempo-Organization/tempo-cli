import pathlib

import rich_click as click

from tempo_core import main_logic, process_management


command_help = "Close the game."

@click.group()
def close():
    """Close related commands"""
    click.echo("Starting close command usage...")

@close.command(name="game", help=command_help, short_help=command_help)
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
def game(settings_json):
    main_logic.close_game()


command_help = "Close the engine."

@close.command(name="engine", help=command_help, short_help=command_help)
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
def engine(settings_json):
    main_logic.close_engine()


command_help = "Closes all programs with the exe names provided."

@close.command(name="programs", help=command_help, short_help=command_help)
@click.option(
    "--exe_names",
    multiple=True,
    type=str,
    required=True,
    help="Name of an executable to be closed, can be specified multiple times.",
)
def programs(exe_names):
    process_management.close_programs(exe_names)
