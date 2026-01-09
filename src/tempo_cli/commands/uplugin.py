import os
import pathlib

import rich_click as click
from tempo_core import main_logic, file_io, settings, app_runner, data_structures


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










# later allow specification of the output directory
command_help = "Build and package one or more uplugins for distribution."

@uplugin.command(name="build", help=command_help, short_help=command_help)
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
    required=False,
    help="Path to the settings JSON file",
)
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
    required=False,
    help="A path to a uplugin to build. Can be specified multiple times.",
)
@click.option(
    "--uplugin_names",
    multiple=True,
    type=str,
    required=False,
    help="A name of a plugin, to build, will be checked for in uproject, then engine install. Can be specified multiple times.",
)
@click.option(
    "--target_platforms",
    multiple=True,
    type=str,
    help="A target platform to target, can be specified multiple times (e.g. Win64).",
    default=['Win64']
)
@click.option(
    "--no_host_platform",
    is_flag=True,
    default=False,
    type=bool,
    help="Prevent compiling for the editor platform on the host",
)
@click.option(
    "--strict_includes",
    is_flag=True,
    default=False,
    type=bool,
    help="Disables precompiled headers and unity build in order to check all source files have self-contained headers.",
)
@click.option(
    "--unversioned",
    is_flag=True,
    default=False,
    type=bool,
    help="Do not embed the current engine version into the descriptor",
)
@click.option(
    "--zip",
    is_flag=True,
    default=False,
    type=bool,
    help="Zips the compiled uplugin(s) into the output directory",
)
def build(
    settings_json,
    uplugin_names,
    uplugin_paths,
    target_platforms,
    no_host_platform,
    strict_includes,
    unversioned,
    zip
):
    final_uplugin_paths = []
    for uplugin_path in uplugin_paths:
        if os.path.isfile(uplugin_path):
            final_uplugin_paths.append(uplugin_path)

    for uplugin_name in uplugin_names:
        potential_path = os.path.normpath(
            f"{os.path.dirname(str(settings.get_uproject_file()))}/Plugins/{uplugin_name}/{uplugin_name}.uplugin"
        )

        if os.path.isfile(potential_path):
            final_uplugin_paths.append(potential_path)
            continue

        engine_plugins_dir = os.path.normpath(
            f"{settings.get_unreal_engine_dir()}/Engine/Plugins"
        )

        uplugin_files = file_io.filter_by_extension(
            file_io.get_files_in_tree(engine_plugins_dir),
            "uplugin"
        )

        matching_plugin = next(
            (
                path for path in uplugin_files
                if os.path.basename(path) == f"{uplugin_name}.uplugin"
            ),
            None
        )

        if matching_plugin:
            final_uplugin_paths.append(matching_plugin)

    if len(final_uplugin_paths) == 0:
        raise RuntimeError("No valid .uplugin files were specified or found.")

    for uplugin_path in list(set(final_uplugin_paths)):
        target_platform_string = '+'.join(set(target_platforms))
        automation_tool = os.path.normpath(f'{settings.get_unreal_engine_dir()}/Engine/Build/BatchFiles/RunUAT.{file_io.get_platform_wrapper_extension()}')
        package_path = os.path.normpath(f'{os.path.dirname(uplugin_path)}/Build') # output to the Build directory inside the directory where the uplugin file is located
        args = [
            'BuildPlugin',
            f'-Plugin="{uplugin_path}"',
            f'-Package="{package_path}"',
            '-Rocket',
            f'TargetPlatform={target_platform_string}'
        ]
        if no_host_platform:
            args.append('-NoHostPlatform')
        if strict_includes:
            args.append('-StrictIncludes')
        if unversioned:
            args.append('-Unversioned')
        exec_mode = data_structures.ExecutionMode.SYNC
        app_runner.run_app(
            exe_path=automation_tool,
            exec_mode=exec_mode,
            args=args
        )
        if zip:
            file_io.zip_directory_tree(package_path, package_path, os.path.normpath(f'{os.path.basename(os.path.dirname(package_path))}.zip'))
