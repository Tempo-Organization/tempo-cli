from pathlib import Path
from typing import Callable
from importlib.metadata import entry_points
import shutil

from tempo_core import env, file_io

if env.getenv("TEMPO_DOCS_BUILD"):
    import click
else:
    import rich_click as click

from tempo_core import app_runner, logger, data_structures
from tempo_core.manager import tools_cache
from tempo_binary_tool_manager import manager


def load_external_tools() -> list[manager.ToolInfo]:
    eps = entry_points(group="tempo.tools")
    tools = []
    for ep in eps:
        tool_cls = ep.load()
        tool = tool_cls(cache=tools_cache)
        tools.append(tool)
    return tools


@click.group()
def tool() -> None:
    """Tool related commands"""


@click.group()
def install() -> None:
    """Install programs"""

def make_tool_install_command(tool_info: manager.ToolInfo) -> Callable:
    tool_name = tool_info.tool_name
    if not tool_name:
        raise RuntimeError('There was not a valid tool name.')
    help_text = f"Install {str(tool_info.tool_name)[0].upper()}{str(tool_info.tool_name)[1:].lower()}"
    @install.command(name=tool_name, help=help_text, short_help=help_text)
    @click.option(
        "--output-directory",
        help="Path to copy the cached tool install to.",
        type=click.Path(resolve_path=True, path_type=Path),
    )
    @click.option(
        "--run-after-install",
        is_flag=True,
        default=False,
        help="Run the installed program after installation.",
    )
    @click.option(
        "--open-tool-directory-in-file-browser",
        is_flag=True,
        default=False,
        help="Whether or not to open the installed tool's directory in the system's file browser.",
    )
    @click.option(
        "--add-tool-to-path",
        is_flag=True,
        default=False,
        help="Whether or not to add the installed tool's directory to the system's PATH environmental variable. Only occurs if you supplied an output directory.",
    )
    def _command(
        output_directory: Path,
        run_after_install: bool,
        open_tool_directory_in_file_browser: bool,
        add_tool_to_path: bool,
    ) -> None:
        tool_info.ensure_tool_installed()
        tool_directory = tool_info.get_tool_directory()
        tool_executable_name = tool_info.get_executable_name()
        if output_directory:
            files_in_tree = file_io.get_files_in_tree(tool_directory)

            for file_path in files_in_tree:
                relative_path = file_path.relative_to(tool_directory)
                output_path = output_directory / relative_path

                output_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, output_path)
            executable_path = (output_directory / tool_directory.joinpath(tool_executable_name).relative_to(tool_directory))
            if add_tool_to_path:
                executable_path_message = f'Adding the following executable "{tool_executable_name}" to the PATH'
                logger.log_message(executable_path_message)
                env.add_path_to_system_environment_path_variable(executable_path.parent)
        else:
            executable_path = tool_info.get_executable_path()

        if open_tool_directory_in_file_browser:
            if output_directory:
                file_io.open_dir_in_file_browser(executable_path.parent)
            else:
                file_io.open_dir_in_file_browser(tool_directory)

        if run_after_install:
            app_runner.run_app(exe_path=executable_path)

    return _command


@click.group()
def uninstall() -> None:
    """Uninstall programs"""


def make_tool_uninstall_command(tool_info: manager.ToolInfo) -> Callable:
    tool_name = tool_info.tool_name
    if not tool_name:
        raise RuntimeError('There was not a valid tool name.')
    uninstall_help_message = f"Uninstall {str(tool_info.tool_name)[0].upper()}{str(tool_info.tool_name)[1:].lower()}"
    @uninstall.command(name=tool_name, help=uninstall_help_message, short_help=uninstall_help_message)
    def _command() -> None:
        repo_name = tool_info.repo_name
        if not repo_name:
            raise RuntimeError('A valid repo name was not provided.')
        tool_name = tool_info.tool_name
        if not tool_name:
            raise RuntimeError('A valid tool name was not provided.')
        tools_cache.uninstall_tool_from_cache(
            repo_name,
            tool_name,
            tool_info.resolve_release_tag(),
        )
    return _command


@click.group()
def run() -> None:
    """Run programs""" 


execution_mode_choices = data_structures.get_enum_strings_from_enum(
        data_structures.ExecutionMode,
    )

def make_tool_run_command(tool_info: manager.ToolInfo) -> Callable:
    tool_name = tool_info.tool_name
    if not tool_name:
        raise RuntimeError('There was not a valid tool name.')
    help_message = f'Command to run {tool_name}'
    @run.command(name=tool_name, help=help_message, short_help=help_message)
    @click.option(
        "--execution-mode",
        help="The execution mode for running the exe.",
        type=click.Choice(execution_mode_choices),
        default=execution_mode_choices[0],
    )
    @click.argument(
        "arguments",
        help="Any amount of arguments you want to pass to the executable.",
        type=str,
        nargs=-1,
    )
    def _command(execution_mode: str, arguments: tuple[str, ...]) -> None:
        tool_info.ensure_tool_installed()
        app_runner.run_app(
            exe_path=tool_info.get_executable_path(),
            exec_mode=data_structures.get_enum_from_val(data_structures.ExecutionMode, execution_mode),
            args=arguments,
        )
    return _command


def make_all_tool_commands() -> None:
    for tool_info in load_external_tools():
        make_tool_install_command(tool_info)
        make_tool_uninstall_command(tool_info)
        make_tool_run_command(tool_info)


make_all_tool_commands()
