from __future__ import annotations
import os
import pathlib

from trogon import tui
import rich_click as click

from tempo_core import (
    file_io,
    initialization
)

from tempo_cli import data_structures as tempo_cli_data_structures
from tempo_cli.commands.tool import tool
from tempo_cli.commands.tool import install
from tempo_cli.commands.dump import dump
from tempo_cli.commands.collection import collection
from tempo_cli.commands.clean import clean
from tempo_cli.commands.close import close
from tempo_cli.commands.file_io import file_io as command_file_io
from tempo_cli.commands.ini import ini
from tempo_cli.commands.init import init
from tempo_cli.commands.json import json
from tempo_cli.commands.mod import mod
from tempo_cli.commands.run import run
from tempo_cli.commands.toml import toml
from tempo_cli.commands.uplugin import uplugin
from tempo_cli.commands.uproject import uproject


default_logs_dir = os.path.normpath(f"{file_io.SCRIPT_DIR}/logs")

rich_color_system_choices = tempo_cli_data_structures.get_enum_strings_from_enum(
        tempo_cli_data_structures.RichColorSystem
    )

@tui()
@click.version_option()
# @click.group(chain=True) disabled to allow easy groups
@click.group()
@click.option(
    "--generate_wrapper",
    is_flag=True,
    default=False,
    type=bool,
    help="Generate a wrapper that contains the current commandline.",
)
@click.option(
    "--disable_log_file_output",
    is_flag=True,
    default=False,
    type=bool,
    help="Whether or not to disable creating log files, defaults to false.",
)
@click.option(
    "--rich_console_color_system",
    default=rich_color_system_choices[0],
    type=click.Choice(rich_color_system_choices),
    help="The color system of the console, uses rich's color system.",
)
@click.option('--log_name_prefix', type=str, help='The log name prefix for your logs.')
@click.option(
    "--logs_directory",
    default=default_logs_dir,
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
    help="The directory you want your logs outputted to.",
)
def cli(
    generate_wrapper,
    disable_log_file_output,
    rich_console_color_system,
    log_name_prefix,
    logs_directory,
    max_content_width=200
):
    initialization.initialization()





cli.add_command(init)

cli.add_command(tool)
tool.add_command(install)

cli.add_command(dump)

cli.add_command(collection)

cli.add_command(clean)

cli.add_command(close)

cli.add_command(command_file_io)

cli.add_command(ini)

cli.add_command(json)

cli.add_command(mod)

cli.add_command(run)

cli.add_command(toml)

cli.add_command(uplugin)

cli.add_command(uproject)
