import os
import pathlib

import rich_click as click

from tempo_core import main_logic


# ---- TOOL GROUP ----
@click.group()
def tool():
    """Tool related commands"""
    click.echo("Starting tool command usage...")

  # attach tool group to main CLI


# ---- INSTALL GROUP ----
@click.group()
def install():
    """Install programs"""
    click.echo("Starting install command usage...")


  # attach install group under tool


# ---- UNINSTALL GROUP (example) ----
# @click.group()
# def uninstall():
#     """Uninstall programs"""
#     click.echo("Starting uninstall command usage...")


# tool.add_command(uninstall)  # attach uninstall group under tool


# ---- INSTALL COMMANDS ----
tools = [
    ("fmodel", "Install FModel", main_logic.install_fmodel),
    ("umodel", "Install Umodel", main_logic.install_umodel),
    ("stove", "Install Stove", main_logic.install_stove),
    ("spaghetti", "Install Spaghetti", main_logic.install_spaghetti),
    ("uasset_gui", "Install UAssetGUI", main_logic.install_uasset_gui),
    ("kismet_analyzer", "Install Kismet Analyzer", main_logic.install_kismet_analyzer),
]

for name, help_text, func in tools:
    @install.command(name=name, help=help_text, short_help=help_text)
    @click.option(
        "--run_after_install",
        is_flag=True,
        default=False,
        type=bool,
        help="Should the installed program be run after installation.",
    )
    @click.argument(
        "output_directory",
        type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
        default=os.path.normpath(f'{os.getcwd()}/tools/{name}')
    )
    def _command(output_directory, run_after_install, func=func):
        func(output_directory=output_directory, run_after_install=run_after_install)
