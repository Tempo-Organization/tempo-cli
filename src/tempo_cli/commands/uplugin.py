import pathlib

import rich_click as click
from tempo_core import main_logic


@click.group()
def uplugin():
    """Uplugin related commands"""


command_help = "Generates a uplugin in a directory, within the specified directory with the given settings."

@uplugin.command(name="generate", help=command_help, short_help=command_help)
@click.option(
    "--can_contain_content",
    default=True,
    type=bool,
    help="Whether the plugin can contain content.",
)
@click.option(
    "--is_installed", default=True, type=bool, help="Whether the plugin is installed."
)
@click.option(
    "--is_hidden", default=False, type=bool, help="Whether the plugin is hidden."
)
@click.option(
    "--no_code",
    default=False,
    type=bool,
    help="Whether the plugin should contain code.",
)
@click.option(
    "--category", default="Modding", type=str, help="Category for the plugin."
)
@click.option(
    "--created_by", default="", type=str, help="Name of the creator of the plugin."
)
@click.option(
    "--created_by_url", default="", type=str, help="URL of the creator of the plugin."
)
@click.option("--description", default="", type=str, help="Description of the plugin.")
@click.option(
    "--docs_url", default="", type=str, help="Documentation URL for the plugin."
)
@click.option(
    "--editor_custom_virtual_path",
    default="",
    type=str,
    help="Custom virtual path for the editor.",
)
@click.option(
    "--enabled_by_default",
    default=True,
    type=str,
    help="Whether the plugin is enabled by default.",
)
@click.option(
    "--engine_major_version",
    default=4,
    type=int,
    help="Major Unreal Engine version for the plugin.",
)
@click.option(
    "--engine_minor_version",
    default=27,
    type=int,
    help="Minor Unreal Engine version for the plugin.",
)
@click.option("--support_url", default="", type=str, help="Support URL for the plugin.")
@click.option("--version", default=1.0, type=float, help="Version of the plugin.")
@click.option(
    "--version_name", default="", type=str, help="Version name of the plugin."
)
@click.argument(
    "plugins_directory",
    type=click.Path(exists=False, resolve_path=True, path_type=pathlib.Path),
)
@click.argument("plugin_name", type=str)
def generate(
    plugins_directory,
    plugin_name,
    can_contain_content,
    is_installed,
    is_hidden,
    no_code,
    category,
    created_by,
    created_by_url,
    description,
    docs_url,
    editor_custom_virtual_path,
    enabled_by_default,
    engine_major_version,
    engine_minor_version,
    support_url,
    version,
    version_name,
):
    """
    Arguments:
        plugins_directory (str): Path to the plugins directory, mainly for use with Uproject plugins folder, and engine plugins folder.
        plugin_name (str): Name of the plugin to be generated.
    """
    main_logic.generate_uplugin(
        plugins_directory=plugins_directory,
        plugin_name=plugin_name,
        category=category,
        created_by=created_by,
        created_by_url=created_by_url,
        description=description,
        docs_url=docs_url,
        editor_custom_virtual_path=editor_custom_virtual_path,
        engine_major_version=engine_major_version,
        engine_minor_version=engine_minor_version,
        support_url=support_url,
        version=version,
        version_name=version_name,
        enabled_by_default=enabled_by_default,
        can_contain_content=can_contain_content,
        is_installed=is_installed,
        is_hidden=is_hidden,
        no_code=no_code,
    )


command_help = "Deletes all files for the specified uplugin paths."

@uplugin.command(name="remove", help=command_help, short_help=command_help)
@click.option(
    "--uplugin_paths",
    multiple=True,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    required=True,
    help="uplugin_paths: A path to a uplugin to delete, can be specified multiple times.",
)
def remove(uplugin_paths):
    main_logic.remove_uplugins(uplugin_paths)
