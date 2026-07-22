import os
import time
import json
from pathlib import Path

import tempo_core.dlc as tc_dlc
from tempo_core import settings

import rich_click as click


@click.group()
def dlc() -> None:
    """DLC related commands"""

@dlc.command(
    name="generate",
    help="Generates a content only dlc plugin in the specified directory with the specified name.",
    short_help="Generates a dlc plugin.",
)
@click.option(
    # the default for this is false, unlike the normal uplugin generate command, as it seems not necessary for the dlc plugins to be read by games, and is not usually enabled for them
    "--is-installed", default=False, type=bool, help="Whether the plugin is installed.",
)
@click.option(
    "--is-hidden", default=False, type=bool, help="Whether the plugin is hidden.",
)
@click.option(
    "--category", default="Modding", type=str, help="Category for the plugin.",
)
@click.option(
    "--created-by", default="", type=str, help="Name of the creator of the plugin.",
)
@click.option(
    "--created-by-url", default="", type=str, help="URL of the creator of the plugin.",
)
@click.option("--description", default="", type=str, help="Description of the plugin.")
@click.option(
    "--docs-url", default="", type=str, help="Documentation URL for the plugin.",
)
@click.option(
    "--editor-custom-virtual-path",
    default="",
    type=str,
    help="Custom virtual path for the editor.",
)
@click.option(
    "--engine-major-version",
    default=4,
    type=int,
    help="Major Unreal Engine version for the plugin.",
)
@click.option(
    "--engine-minor-version",
    default=27,
    type=int,
    help="Minor Unreal Engine version for the plugin.",
)
@click.option("--support-url", default="", type=str, help="Support URL for the plugin.")
@click.option("--version", default=1.0, type=float, help="Version of the plugin.")
@click.option(
    "--version-name", default="", type=str, help="Version name of the plugin.",
)
@click.argument(
    "plugins-directory",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
)
@click.argument("plugin-name", type=str)

# below shouldn't be required, only needed if a full path wasn't specified for the archive dir,
# though maybe this should just go to working dir instead to append if that is not present.
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file.",
)
def generate(
    plugin_name: str,
    plugins_directory: Path,
    engine_major_version: int,
    engine_minor_version: int,
    is_installed: bool,
    is_hidden: bool,
    category: str,
    created_by: str,
    created_by_url: str,
    description: str,
    docs_url: str,
    editor_custom_virtual_path: str,
    support_url: str,
    version: float,
    version_name: str,
    config_file: Path,
) -> None:
    tc_dlc.generate_dlc_plugin(
        plugins_directory=plugins_directory,
        plugin_name=plugin_name,
        category=category,
        created_by=created_by,
        created_by_url=created_by_url,
        description=description,
        docs_url=docs_url,
        editor_custom_virtual_path=editor_custom_virtual_path,
        unreal_engine_major_version=engine_major_version,
        unreal_engine_minor_version=engine_minor_version,
        support_url=support_url,
        version=version,
        version_name=version_name,
        is_installed=is_installed,
        is_hidden=is_hidden,
    )


@dlc.command(
    name="build",
    help="Builds the content only dlc plugin with the specified name.",
    short_help="Builds a dlc plugin.",
)
@click.argument("plugin-name", type=str, required=True)
@click.argument("release-version", type=str, required=True)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file.",
)
def build(
    plugin_name: str,
    release_version: str,
    config_file: Path,
) -> None:
    tc_dlc.build_dlc_plugin(
        plugin_name=plugin_name,
        release_version=release_version,
)


@dlc.command(
    name="make-base-release",
    help="",
    short_help="",
)
@click.argument("release-version", type=str, required=True)
@click.argument(
    "archive-directory",
    type=click.Path(exists=False, resolve_path=True, path_type=Path),
    default=Path("Packages/BaseRelease"),
)
@click.option(
    "--config-file",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=Path,
    ),
    required=True,
    help="Path to the tempo config file.",
)
def make_base_release(
    release_version: str,
    archive_directory: Path,
    config_file: Path,
) -> None:
    if not archive_directory.is_absolute():
        uproject_file = settings.get_uproject_file()
        if not uproject_file:
            uproject_not_found_error = (
                f'could not find the specified uproject file "{uproject_file}"'
            )
            raise FileNotFoundError(uproject_not_found_error)
        archive_directory = uproject_file.parent / archive_directory
    tc_dlc.make_base_release(
        archive_dir=archive_directory,
        release_version=release_version,
)
