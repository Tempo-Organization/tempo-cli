import pathlib

import tomlkit
import rich_click as click
from tempo_core import logger


@click.group()
def toml():
    """Toml related commands"""
    click.echo("Starting toml command usage...")


command_help_add_toml = "Add an entry to a TOML file."

@toml.command(
    name="add", help=command_help_add_toml, short_help=command_help_add_toml
)
@click.option(
    "--toml_path",
    help="Path to the TOML file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option("--key", help="Key to add to the TOML file.", type=str, required=True)
@click.option(
    "--value", help="Value to associate with the key.", type=str, required=True
)
def add(toml_path, key, value):
    with toml_path.open("r+") as f:
        data = tomlkit.load(f)
        data[key] = value
        f.seek(0)
        f.write(tomlkit.dumps(data))
        f.truncate()
    logger.log_message(f"Added {key}: {value} to {toml_path}.")


command_help_remove_toml = "Remove an entry from a TOML file."


@toml.command(
    name="remove",
    help=command_help_remove_toml,
    short_help=command_help_remove_toml,
)
@click.option(
    "--toml_path",
    help="Path to the TOML file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--key", help="Key to remove from the TOML file.", type=str, required=True
)
def remove(toml_path, key):
    with toml_path.open("r+") as f:
        data = tomlkit.load(f)
        if key in data:
            del data[key]
            f.seek(0)
            f.write(tomlkit.dumps(data))
            f.truncate()
            logger.log_message(f"Removed {key} from {toml_path}.")
        else:
            logger.log_message(f"Key {key} not found in {toml_path}.")
