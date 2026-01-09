import pathlib

import rich_click as click

from tempo_core import unreal_inis


@click.group()
def ini():
    """Ini related commands"""
    click.echo("Starting ini command usage...")


command_help = (
    "Adds the specified tags to the ini's MetaDataTagsForAssetRegistry= section."
)

@ini.command(
    name="add_meta_data_tags_for_asset_registry_to_unreal_ini",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--ini_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the ini file to edit.",
    required=True,
)
@click.option(
    "--tags",
    type=str,
    help="The new tags to add to the ini under the MetaDataTagsForAssetRegistry= section.",
    multiple=True,
    default=[],
)
def add_meta_data_tags_for_asset_registry_to_unreal_ini(
    ini_path: pathlib.Path, tags: list[str]
):
    unreal_inis.add_meta_data_tags_for_asset_registry_to_unreal_ini(
        ini=ini_path, tags=tags
    )


command_help = (
    "Removes the specified tags to the ini's MetaDataTagsForAssetRegistry= section."
)

@ini.command(
    name="remove_meta_data_tags_for_asset_registry_from_unreal_ini",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--ini_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the ini file to edit.",
    required=True,
)
@click.option(
    "--tags",
    type=str,
    help="The new tags to remove from the ini under the MetaDataTagsForAssetRegistry= section.",
    multiple=True,
    default=[],
)
def remove_meta_data_tags_for_asset_registry_from_unreal_ini(
    ini_path: pathlib.Path, tags: list[str]
):
    unreal_inis.remove_meta_data_tags_for_asset_registry_from_unreal_ini(
        ini=ini_path, tags=tags
    )
