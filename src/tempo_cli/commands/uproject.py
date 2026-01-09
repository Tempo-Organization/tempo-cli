import pathlib

import rich_click as click
from tempo_core import main_logic


@click.group()
def uproject():
    """Uproject related commands"""
    click.echo("Starting uproject command usage...")


command_help = (
    "Generates a uproject file at the specified location, using the given information."
)


@uproject.command(name="generate", help=command_help, short_help=command_help)
@click.option(
    "--file_version",
    default=3,
    type=int,
    help="Uproject file specification. Defaults to 3.",
)
@click.option(
    "--engine_major_association",
    default=4,
    type=int,
    help="Major Unreal Engine version for the project. Example: the 4 in 4.27.",
)
@click.option(
    "--engine_minor_association",
    default=27,
    type=int,
    help="Minor Unreal Engine version for the project. Example: the 27 in 4.27.",
)
@click.option(
    "--category", default="Modding", type=str, help="Category for the uproject."
)
@click.option(
    "--description",
    default="Uproject for modding, generated with tempo.",
    type=str,
    help="Description for the uproject.",
)
@click.option(
    "--ignore_safety_checks",
    default=False,
    type=bool,
    help="Whether or not to override the input checks for this command.",
)
@click.argument(
    "project_file",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
)
def generate(
    project_file,
    file_version,
    engine_major_association,
    engine_minor_association,
    category,
    description,
    ignore_safety_checks,
):
    """
    Arguments:
        project_file (str): Path to generate the project file at.
    """
    main_logic.generate_uproject(
        project_file=project_file,
        file_version=file_version,
        engine_major_association=engine_major_association,
        engine_minor_association=engine_minor_association,
        category=category,
        description=description,
        ignore_safety_checks=ignore_safety_checks,
    )




command_help = "Resaves packages and fixes up redirectors for the project."


@uproject.command(
    name="resave_packages_and_fix_up_redirectors",
    help=command_help,
    short_help=command_help,
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
def resave_packages_and_fix_up_redirectors(settings_json):
    main_logic.resave_packages_and_fix_up_redirectors()

command_help = "Builds the uproject specified within the settings JSON"
@uproject.command(name="build", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Will close engine instances at the start and open at the end of the command process",
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
def build(settings_json, toggle_engine):
    main_logic.build(toggle_engine=toggle_engine)


command_help = "Cooks content for the uproject specified within the settings JSON"


@uproject.command(name="cook", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Will close engine instances at the start and open at the end of the command process",
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
def cook(settings_json, toggle_engine):
    main_logic.cook(toggle_engine=toggle_engine)


command_help = "Package content for the uproject specified within the settings JSON"


@uproject.command(name="package", help=command_help, short_help=command_help)
@click.option(
    "--toggle_engine",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to close engine instances at the start and open at the end of the command process",
)
@click.option(
    "--use_symlinks",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to use symlinks to save time with file operations",
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
def package(settings_json, toggle_engine, use_symlinks):
    main_logic.package(toggle_engine=toggle_engine, use_symlinks=use_symlinks)
