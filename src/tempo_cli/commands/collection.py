import os
import pathlib

import rich_click as click

from tempo_core import data_structures, unreal_collections


file_content_options = data_structures.get_enum_strings_from_enum(
    unreal_collections.UnrealContentLineType
)
command_help = "Create Collection"
default_create_collection_guid = unreal_collections.UnrealGuid.generate_unreal_guid()
default_parent_guid = unreal_collections.get_blank_unreal_guid().to_uid()

@click.group()
def collection():
    """Collection related commands"""
    click.echo("Starting collection command usage...")

@collection.command(name="create_collection", help=command_help, short_help=command_help)
@click.option(
    "--collection_path",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
    help="The path to the collection file to edit.",
    required=True,
)
@click.option(
    "--file_version", type=int, default=2, help="The collection file version."
)
@click.option(
    "--content_type",
    default=file_content_options[0],
    type=click.Choice(file_content_options),
    help="The type of content collection, dynamic uses file filters, static uses manual specification",
)
@click.option(
    "--guid",
    default=default_create_collection_guid,
    type=str,
    help="The guid of the collection, if not provided one will be automatically generated.",
)
@click.option(
    "--parent_guid",
    default=default_parent_guid,
    type=str,
    help="The parent guid of the collection, if not provided no parent is assumed, and a blank one is given.",
)
@click.option(
    "--red", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--green", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--blue", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--alpha", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--file_paths",
    type=str,
    multiple=True,
    help="A list of file paths to include in the collection, they will be automatically converted into unreal asset paths. For use with static collections.",
)
@click.option(
    "--unreal_asset_paths",
    type=str,
    multiple=True,
    help="A list of unreal asset paths for the collection, for static collections.",
)
@click.option(
    "--filter_lines",
    type=str,
    multiple=True,
    help="A list of asset filter for the collection, for use with dynamic collections.",
)
def create_collection(
    collection_path: pathlib.Path,
    file_version: int,
    content_type: str,
    guid: str,
    parent_guid: str,
    red: float,
    green: float,
    blue: float,
    alpha: float,
    file_paths: list[str],
    unreal_asset_paths: list[str],
    filter_lines: list[str],
):
    type_of_content = data_structures.get_enum_from_val(
        unreal_collections.UnrealContentLineType, content_type
    )
    content_lines = []
    os.makedirs(os.path.dirname(collection_path), exist_ok=True)
    if type_of_content == unreal_collections.UnrealContentLineType.STATIC:
        for file_path in file_paths:
            content_lines.append(unreal_collections.UnrealAssetPath(path=file_path))
        for unreal_asset_path in unreal_asset_paths:
            content_lines.append(
                unreal_collections.UnrealAssetPath(
                    unreal_collections.UnrealAssetPath.static_from_asset_reference(
                        unreal_asset_path
                    )
                )
            )
    if type_of_content == unreal_collections.UnrealContentLineType.DYNAMIC:
        content_lines = filter_lines
    unreal_collections.create_collection(
        collection_name=os.path.basename(collection_path),
        collections_directory=pathlib.Path(os.path.dirname(collection_path)),
        file_version=file_version,
        collection_type=unreal_collections.UnrealContentLineType(type_of_content),
        guid=unreal_collections.UnrealGuid.from_uid(guid),
        parent_guid=unreal_collections.UnrealGuid.from_uid(parent_guid),
        color=unreal_collections.UnrealCollectionColor(r=red, g=green, b=blue, a=alpha),
        content_lines=content_lines,
        exist_ok=True,
    )


command_help = "Set Collection Color"


@collection.command(
    name="set_color_from_collection_path", help=command_help, short_help=command_help
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to edit.",
    required=True,
)
@click.option(
    "--red", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--green", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--blue", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
@click.option(
    "--alpha", default=0.0, type=float, help="The value of the color, accepts 0.0-1.0."
)
def set_color_from_collection_path(
    collection_path: pathlib.Path, red: float, green: float, blue: float, alpha: float
):
    unreal_collections.set_color_from_collection_path(
        collection_path,
        unreal_collections.UnrealCollectionColor(r=red, g=green, b=blue, a=alpha),
    )


command_help = "Rename Collection"


@collection.command(name="rename_collection", help=command_help, short_help=command_help)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
@click.option(
    "--new_name", type=str, help="New name for the collection.", required=True
)
def rename_collection(collection_path: str, new_name: str):
    unreal_collections.rename_collection_from_collection_path(pathlib.Path(collection_path), new_name)


command_help = "Delete Collection"


@collection.command(name="delete_collection", help=command_help, short_help=command_help)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
def delete_collection(collection_path: str):
    unreal_collections.delete_collection(collection_path)


command_help = "Disable Collection"


@collection.command(name="disable_collection", help=command_help, short_help=command_help)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
def disable_collection(collection_path: str):
    unreal_collections.disable_collection(collection_path)


command_help = "Enable Collection"


@collection.command(name="enable_collection", help=command_help, short_help=command_help)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
def enable_collection(collection_path: str):
    unreal_collections.enable_collection(unreal_collections.get_unreal_collection_from_unreal_collection_path(pathlib.Path(collection_path)))


command_help = "Set Guid"
default_set_guid_from_collection_path_guid = unreal_collections.UnrealGuid.to_uid(
    unreal_collections.UnrealGuid(unreal_collections.UnrealGuid.generate_unreal_guid())
)


@collection.command(
    name="set_guid_from_collection_path", help=command_help, short_help=command_help
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
@click.option(
    "--guid",
    default=default_set_guid_from_collection_path_guid,
    type=str,
    help="The new guid in string form for the collection.",
)
def set_guid_from_collection_path(collection_path: str, guid: str):
    unreal_collections.set_guid_from_collection_path(
        collection_path=pathlib.Path(collection_path),
        guid=unreal_collections.UnrealGuid.from_uid(guid),
    )


command_help = "Set Parent Guid"


@collection.command(
    name="set_parent_guid_from_collection_path",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to rename.",
    required=True,
)
@click.option(
    "--parent_guid",
    default=default_parent_guid,
    type=str,
    help="The new parent guid in string form for the collection.",
)
def set_parent_guid_from_collection_path(collection_path: str, parent_guid: str):
    unreal_collections.set_parent_guid_from_collection_path(
        collection_path=pathlib.Path(collection_path),
        parent_guid=unreal_collections.UnrealGuid(parent_guid),
    )


command_help = "Set File Version"


@collection.command(
    name="set_file_version_from_collection_path",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to change the file version of.",
    required=True,
)
@click.option(
    "--file_version",
    default=2,
    type=int,
    help="The new file version for the collection.",
)
def set_file_version_from_collection_path(collection_path: str, file_version: int):
    unreal_collections.set_file_version_from_collection_path(collection_path=pathlib.Path(collection_path), file_version=file_version)


set_content_type_options = data_structures.get_enum_strings_from_enum(
    unreal_collections.UnrealContentLineType
)
command_help = "Set Collection Type"


@collection.command(
    name="set_collection_type_from_collection_path",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to change the file version of.",
    required=True,
)
@click.option(
    "--collection_type",
    default=unreal_collections.UnrealContentLineType.STATIC.value,
    type=click.Choice(set_content_type_options),
    help="The new content type for the collection, Static or Dynamic.",
)
def set_collection_type_from_collection_path(
    collection_path: str, collection_type: str
):
    type_to_pass = data_structures.get_enum_from_val(
        unreal_collections.UnrealContentLineType, collection_type
    )
    unreal_collections.set_collection_type_from_collection_path(
        collection_path=pathlib.Path(collection_path), collection_type=unreal_collections.UnrealContentLineType(type_to_pass)
    )


command_help = "Add content lines to collection file, Dynamic accepts filter lines, while Static accepts content path lines and unreal asset path lines"


@collection.command(
    name="add_content_lines_to_collection", help=command_help, short_help=command_help
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to edit.",
    required=True,
)
@click.option(
    "--content_path_lines",
    type=str,
    help="The new content lines to add to the collection, they will be converted to unreal asset paths.",
    multiple=True,
    default=[],
)
@click.option(
    "--filter_lines",
    type=str,
    help="The new content filter lines to add to the collection.",
    multiple=True,
    default=[],
)
@click.option(
    "--unreal_asset_paths",
    type=str,
    help="The new unreal asset path lines to add to the collection.",
    multiple=True,
    default=[],
)
def add_content_lines_to_collection(
    collection_path: str,
    content_path_lines: list[str],
    filter_lines: list[str],
    unreal_asset_paths: list[str],
):
    collection = unreal_collections.get_unreal_collection_from_unreal_collection_path(
        pathlib.Path(collection_path)
    )
    collection_type = collection.content_type
    content_lines = []
    if collection_type == unreal_collections.UnrealContentLineType.DYNAMIC:
        content_lines.extend(filter_lines)

    if collection_type == unreal_collections.UnrealContentLineType.STATIC:
        for content_path_line in content_path_lines:
            content_lines.append(unreal_collections.UnrealAssetPath(content_path_line))

        for unreal_asset_path in unreal_asset_paths:
            test_one = unreal_collections.UnrealAssetPath.static_from_asset_reference(
                unreal_asset_path
            )
            test_two = unreal_collections.UnrealAssetPath(test_one)
            content_lines.append(test_two)
    unreal_collections.add_content_lines_to_collection(
        collection=collection, content_lines=content_lines
    )


command_help = "Remove content lines from collection file, Dynamic accepts filter lines, while Static accepts content path lines and unreal asset path lines"


@collection.command(
    name="remove_content_lines_from_collection",
    help=command_help,
    short_help=command_help,
)
@click.option(
    "--collection_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to the collection file to edit.",
    required=True,
)
@click.option(
    "--content_path_lines",
    type=str,
    help="The new content lines to remove from the collection, they will be converted to unreal asset paths.",
    multiple=True,
    default=[],
)
@click.option(
    "--filter_lines",
    type=str,
    help="The new content filter lines to remove from the collection.",
    multiple=True,
    default=[],
)
@click.option(
    "--unreal_asset_paths",
    type=str,
    help="The new unreal asset path lines to remove from the collection.",
    multiple=True,
    default=[],
)
def remove_content_lines_from_collection(
    collection_path: str,
    content_path_lines: list[str],
    filter_lines: list[str],
    unreal_asset_paths: list[str],
):
    collection = unreal_collections.get_unreal_collection_from_unreal_collection_path(
        pathlib.Path(collection_path)
    )
    content_lines = []

    if collection.content_type == unreal_collections.UnrealContentLineType.DYNAMIC:
        content_lines.extend(filter_lines)

    if collection.content_type == unreal_collections.UnrealContentLineType.STATIC:
        for content_path_line in content_path_lines:
            content_lines.append(unreal_collections.UnrealAssetPath(content_path_line))

        for unreal_asset_path in unreal_asset_paths:
            content_lines.append(
                unreal_collections.UnrealAssetPath(
                    unreal_collections.UnrealAssetPath.static_from_asset_reference(
                        unreal_asset_path
                    )
                )
            )

    unreal_collections.remove_content_lines_from_collection(
        collection=collection, content_lines=content_lines
    )


command_help = "Add collections to the mod entry in the settings json"


@collection.command(
    name="add_collections_to_mod_entry", help=command_help, short_help=command_help
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
    help="The path to the settings json, who's mod entry you want to add collections to.",
    required=True,
)
@click.option(
    "--mod_name",
    type=str,
    help="The mod name of the mod entry in the settings json to add the collection(s) to.",
    required=True,
)
@click.option(
    "--collection_paths",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to a collection to add to the settings json, can be specified multiple times.",
    default=[],
    multiple=True,
)
def add_collections_to_mod_entry(
    settings_json: pathlib.Path, mod_name: str, collection_paths: list[pathlib.Path]
):
    collections_to_pass = []
    for collection_path in collection_paths:
        collections_to_pass.append(
            unreal_collections.get_unreal_collection_from_unreal_collection_path(
                collection_path
            )
        )
    unreal_collections.add_collections_to_mod_entry(
        collections_to_pass, mod_name, settings_json
    )


command_help = "Remove collections to the mod entry in the settings json"


@collection.command(
    name="remove_collections_from_mod_entry", help=command_help, short_help=command_help
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
    help="The path to the settings json, who's mod entry you want to remove collections from.",
    required=True,
)
@click.option(
    "--mod_name",
    type=str,
    help="The mod name of the mod entry in the settings json to remove the collection(s) from.",
    required=True,
)
@click.option(
    "--collection_paths",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    help="The path to a collection to remove from the settings json, can be specified multiple times.",
    default=[],
    multiple=True,
)
def remove_collections_from_mod_entry(
    settings_json: pathlib.Path, mod_name: str, collection_paths: list[pathlib.Path]
):
    collections_to_pass = []
    for collection_path in collection_paths:
        collections_to_pass.append(
            unreal_collections.get_unreal_collection_from_unreal_collection_path(
                collection_path
            )
        )
    unreal_collections.remove_collections_from_mod_entry(
        collections_to_pass, mod_name, settings_json
    )
