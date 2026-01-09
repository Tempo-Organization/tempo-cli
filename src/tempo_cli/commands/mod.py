import os
import pathlib

import rich_click as click
from tempo_core import main_logic, data_structures, settings, file_io


default_output_releases_dir = os.path.normpath(os.path.join(file_io.SCRIPT_DIR, "dist"))
default_releases_dir = os.path.normpath(
    os.path.join(
        str(settings.settings_information.settings_json_dir), "mod_packaging", "releases"
    )
)


@click.group()
def mod():
    """Mod related commands"""


command_help = "Enable the given mod name in the provided settings JSON."

@mod.command(name="enable_mod", help=command_help, short_help=command_help)
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
    "--mod_name",
    type=str,
    required=True,
    help="Name of a mod to enable, can be specified multiple times",
    prompt="What is the name of the mod you want to enable? "
)
def enable_mod(settings_json, mod_name):
    main_logic.enable_mods(settings_json=settings_json, mod_names=[mod_name])


command_help = "Enable the given mod names in the provided settings JSON."


@mod.command(name="enable_mods", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="Name of a mod to enable, can be specified multiple times",
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
def enable_mods(settings_json, mod_names):
    main_logic.enable_mods(settings_json=settings_json, mod_names=mod_names)


command_help = "Disable the given mod names in the provided settings JSON."


@mod.command(name="disable_mods", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="Name of a mod to disable, can be specified multiple times",
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
def disable_mods(settings_json, mod_names):
    main_logic.disable_mods(settings_json=settings_json, mod_names=mod_names)


command_help = "Disable the given mod names in the provided settings JSON."


@mod.command(name="disable_mod", help=command_help, short_help=command_help)
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
    "--mod_name",
    type=str,
    required=True,
    help="Name of a mod to disable, can be specified multiple times",
    prompt="What is the name of the mod you want to disable?"
)
def disable_mod(settings_json, mod_name):
    main_logic.disable_mods(settings_json=settings_json, mod_names=[mod_name])


command_help = "Adds the given mod name in the provided settings JSON."

packing_type_choices = data_structures.get_enum_strings_from_enum(
    data_structures.PackingType
)

@mod.command(name="add_mod", help=command_help, short_help=command_help)
@click.option("--mod_name", type=str, required=True, prompt="What is your mod name?")
@click.option("--pak_dir_structure", type=str, required=True, prompt="What is your pak dir structure? If left blank, defaults to ", default="~mods")
@click.option(
    "--packing_type",
    type=click.Choice(packing_type_choices),
    help="Packing type for the mod.",
    required=True,
    default=packing_type_choices[1],
    prompt="What will be the packaging method for your mod? If left blank, defaults to "
)
@click.option(
    "--mod_name_dir_type",
    type=str,
    default="Mods",
    help='Directory type for the mod name (default: "Mods").',
    required=True,
    prompt="What is the directory name for your mod type? e.g. The Mods in Content/Mods/ModName or CustomContent in Content/CustomContent/ModName, or another pattern. If left blank, defaults to "
)
@click.option(
    "--mod_name_dir_name_override",
    type=str,
    default="",
    help="Override the mod name directory with this value (optional).",
    required=True,
    prompt="if you need one, what is your mod name dir name override? Useful for Content/Mods/ModName but having ModName_P.pak for example. If left blank, defaults to None and uses the mod_name"
)
@click.option(
    "--pak_chunk_num",
    type=int,
    default=0,
    help="Pak chunk number (optional).",
    required=True,
    prompt="If you are using the engine packing method, what is your mod's chunk id? If left blank, defaults to "
)
@click.option(
    "--compression_type",
    default="",
    type=str,
    help="Compression type for the mod (optional).",
    required=True,
    prompt="What if any is your compression method for packing? If left blank, defaults to None"
)
@click.option(
    "--is_enabled",
    type=bool,
    default=True,
    help="Whether the mod is enabled (default: True).",
)
@click.option(
    "--asset_paths",
    multiple=True,
    help="Asset path for the mod, can be specified multiple times.",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--tree_paths",
    multiple=True,
    help="Tree path for the mod, can be specified multiple times.",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
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
    prompt="What is the path to your tempo config file?"
)


def add_mod(
    settings_json,
    mod_name,
    packing_type,
    pak_dir_structure,
    mod_name_dir_type,
    mod_name_dir_name_override,
    pak_chunk_num,
    compression_type,
    is_enabled,
    asset_paths,
    tree_paths,
):
    if pak_chunk_num == 0:
        pak_chunk_num = None
    if mod_name_dir_name_override == "":
        mod_name_dir_name_override = None
    if compression_type == "":
        compression_type = None
    main_logic.add_mod(
        settings_json=settings_json,
        mod_name=mod_name,
        packing_type=packing_type,
        pak_dir_structure=pak_dir_structure,
        mod_name_dir_type=mod_name_dir_type,
        mod_name_dir_name_override=mod_name_dir_name_override,
        pak_chunk_num=pak_chunk_num,
        compression_type=compression_type,
        is_enabled=is_enabled,
        asset_paths=asset_paths,
        tree_paths=tree_paths,
    )


command_help = "Remove the given mod name in the provided settings JSON."


@mod.command(name="remove_mod", help=command_help, short_help=command_help)
@click.option(
    "--mod_name",
    type=str,
    required=True,
    help="Name of a mod to be removed.",
    prompt="What is the name of the mod to remove?"
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
def remove_mod(settings_json, mod_name):
    main_logic.remove_mods(settings_json=settings_json, mod_names=[mod_name])


command_help = "Removes the given mod names in the provided settings JSON."


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
def remove_mods(settings_json, mod_names):
    main_logic.remove_mods(settings_json=settings_json, mod_names=mod_names)



command_help = "Generates mods for the specified mod names."


@mod.command(name="generate_mods", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="A mod name, can be specified multiple times",
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
def generate_mods(settings_json, mod_names, use_symlinks):
    main_logic.generate_mods(input_mod_names=mod_names, use_symlinks=use_symlinks)


command_help = "Generates mods for all enabled mods within the specified settings JSON."


@mod.command(name="generate_mods_all", help=command_help, short_help=command_help)
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
def generate_mods_all(settings_json, use_symlinks):
    main_logic.generate_mods_all(use_symlinks=use_symlinks)


command_help = "Generate one or more mod releases."


@mod.command(name="generate_mod_releases", help=command_help, short_help=command_help)
@click.option(
    "--mod_names",
    multiple=True,
    type=str,
    required=True,
    help="A mod name, can be specified multiple times",
)
@click.option(
    "--base_files_directory",
    default=default_releases_dir,
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--output_directory",
    default=default_output_releases_dir,
    help="Path to the output directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
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
def generate_mod_releases(
    settings_json, mod_names, base_files_directory, output_directory
):
    main_logic.generate_mod_releases(mod_names, base_files_directory, output_directory)


command_help = "Generate mod releases for all mods within the specified settings JSON."


@mod.command(
    name="generate_mod_releases_all", help=command_help, short_help=command_help
)
@click.option(
    "--base_files_directory",
    default=default_releases_dir,
    help="Path to dir tree whose content to pack alongside the mod for release",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--output_directory",
    default=default_output_releases_dir,
    help="Path to the output directory",
    type=click.Path(
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
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
def generate_mod_releases_all(settings_json, base_files_directory, output_directory):
    main_logic.generate_mod_releases_all(base_files_directory, output_directory)
