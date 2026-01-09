import json as json_module
import pathlib

import rich_click as click
from tempo_core import logger


@click.group()
def json():
    """Json related commands"""
    click.echo("Starting json command usage...")


command_help_add_json = "Add an entry to a JSON file."

@json.command(
    name="add", help=command_help_add_json, short_help=command_help_add_json
)
@click.option(
    "--json_path",
    help="Path to the JSON file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option("--key", help="Key to add to the JSON file.", type=str, required=True)
@click.option(
    "--value", help="Value to associate with the key.", type=str, required=True
)
def add(json_path, key, value):
    with json_path.open("r+") as f:
        data = json_module.load(f)
        data[key] = value
        f.seek(0)
        json_module.dump(data, f, indent=4)
        f.truncate()
    logger.log_message(f"Added {key}: {value} to {json_path}.")


command_help_remove_json = "Remove an entry from a JSON file."

@json.command(
    name="remove",
    help=command_help_remove_json,
    short_help=command_help_remove_json,
)
@click.option(
    "--json_path",
    help="Path to the JSON file.",
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path),
    required=True,
)
@click.option(
    "--key", help="Key to remove from the JSON file.", type=str, required=True
)
def remove(json_path, key):
    with json_path.open("r+") as f:
        data = json_module.load(f)
        if key in data:
            del data[key]
            f.seek(0)
            json_module.dump(data, f, indent=4)
            f.truncate()
            logger.log_message(f"Removed {key} from {json_path}.")
        else:
            logger.log_message(f"Key {key} not found in {json_path}.")
