import os
import time
import json
import pathlib

from tempo_core import main_logic, window_management, utilities, game_runner, logger
from tempo_core.programs import retoc, pattern_sleuth
from tempo_core.programs import jmap as jmap_tool
from tempo_core.threads import game_monitor

import rich_click as click


@click.group()
def dump():
    """Dump related commands"""

@dump.command(
    name="aes_keys",
    help="Dumps the aes key(s) from the game in the provided settings json.",
    short_help="Dumps the key(s) from the game in the provided settings json.",
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
@click.option(
    "--directory",
    default=os.getcwd(),
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path, file_okay=False, dir_okay=True),
    help="The directory you want your aes key outputted to.",
)
@click.option(
    "--dump_to_tempo_config",
    type=bool,
    default=True,
    help="Whether the dumped info should be stored in the tempo config file or not.",
)
def aes_keys(settings_json, directory, dump_to_tempo_config):
    if not pattern_sleuth.is_current_preferred_patternsleuth_version_installed():
        pattern_sleuth.install_tool_patternsleuth()

    aes_keys = []
    for key in pattern_sleuth.run_patternsleuth_aes_key_scan_command():
        logger.log_message(f"AES Key: {key}")
        if key not in aes_keys:
            aes_keys.append(key)

    os.makedirs(directory, exist_ok=True)

    output_path = os.path.join(directory, "aes_keys.json")

    data = {
        "aes_keys": aes_keys
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    logger.log_message(f'output path: {output_path}')

    if not dump_to_tempo_config:
        return

    with open(settings_json, "r", encoding="utf-8") as f:
        settings = json.load(f)

    engine_info = settings.setdefault("engine_info", {})

    engine_info["aes_keys"] = aes_keys

    with open(settings_json, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

    logger.log_message(f"updated settings json: {settings_json}")


@dump.command(
    name="engine_version",
    help="Dumps the engine version from the game in the provided settings json.",
    short_help="Dumps the engine version from the game in the provided settings json.",
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
@click.option(
    "--directory",
    default=os.getcwd(),
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path, file_okay=False, dir_okay=True),
    help="The directory you want your engine version outputted to.",
)
@click.option(
    "--dump_to_tempo_config",
    type=bool,
    default=True,
    help="Whether the dumped info should be stored in the tempo config file or not.",
)
def engine_version(settings_json, directory, dump_to_tempo_config):

    if not pattern_sleuth.is_current_preferred_patternsleuth_version_installed():
        pattern_sleuth.install_tool_patternsleuth()

    info = pattern_sleuth.run_patternsleuth_engine_version_scan_command()

    if not info:
        raise RuntimeError('dump engine version command failed due to info being None.')

    os.makedirs(directory, exist_ok=True)

    output_path = os.path.join(directory, "engine_version.json")

    data = {
        "engine_major_version": info["major"],
        "engine_minor_version": info["minor"]
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    logger.log_message(f'output path: {output_path}')

    if not dump_to_tempo_config:
        return

    with open(settings_json, "r", encoding="utf-8") as f:
        settings = json.load(f)

    engine_info = settings.setdefault("engine_info", {})

    engine_info["unreal_engine_major_version"] = info["major"]
    engine_info["unreal_engine_minor_version"] = info["minor"]

    with open(settings_json, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

    logger.log_message(f"updated settings json: {settings_json}")


@dump.command(
    name="build_configuration",
    help="Dumps the build configuration from the game in the provided settings json.",
    short_help="Dumps the build configuration from the game in the provided settings json.",
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
@click.option(
    "--directory",
    default=os.getcwd(),
    type=click.Path(exists=True, resolve_path=True, path_type=pathlib.Path, file_okay=False, dir_okay=True),
    help="The directory you want your build configuration outputted to.",
)
@click.option(
    "--dump_to_tempo_config",
    type=bool,
    default=True,
    help="Whether the dumped info should be stored in the tempo config file or not.",
)
def build_configuration(settings_json, directory, dump_to_tempo_config):

    if not pattern_sleuth.is_current_preferred_patternsleuth_version_installed():
        pattern_sleuth.install_tool_patternsleuth()

    info = pattern_sleuth.run_patternsleuth_build_configuration_scan_command()

    if not info:
        raise RuntimeError('dump build configuration command failed due to info being None.')

    os.makedirs(directory, exist_ok=True)

    output_path = os.path.join(directory, "build_configuration.json")

    data = {
        "build_configuration": info
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    logger.log_message(output_path)

    if not dump_to_tempo_config:
        return

    with open(settings_json, "r", encoding="utf-8") as f:
        settings = json.load(f)

    engine_info = settings.setdefault("engine_info", {})

    engine_info["build_configuration"] = info

    with open(settings_json, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

    logger.log_message(f"updated settings json: {settings_json}")


@dump.command(
    name="jmap",
    help="Dumps the jmap from the game in the provided settings json.",
    short_help="Dumps the jmap from the game in the provided settings json.",
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
@click.option(
    "--output",
    default=os.path.normpath(f'{os.getcwd()}/Modding/output.jmap'),
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    help="The file location you want your jmap outputted to.",
)
def jmap(settings_json, output):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    if not jmap_tool.is_current_preferred_jmap_version_installed():
        jmap_tool.install_tool_jmap()

    game_runner.run_game()
    game_monitor.start_game_monitor_thread()

    window_title_override = utilities.get_game_window_title()
    if not window_title_override:
        game_monitor.stop_game_monitor_thread()
        raise RuntimeError('There was no provided window title override')

    timeout = 45.0
    poll_interval = 0.1
    elapsed = 0.0

    while elapsed < timeout:
        info = game_monitor.game_monitor_thread_information

        if info.found_window and info.found_process:
            break

        time.sleep(poll_interval)
        elapsed += poll_interval
    else:
        game_monitor.stop_game_monitor_thread()
        raise RuntimeError('Timed out waiting for game window/process')

    game_pid = window_management.get_pid_from_window_title(window_title_override)
    if not game_pid:
        game_monitor.stop_game_monitor_thread()
        raise RuntimeError('There was no valid game pid passed to the command.')

    # sometimes if you scan right when game opens errors occur, so a bit of a delay, make this configurable later somehow
    time.sleep(3)

    jmap_tool.run_dump_jmap_jmap_command(
        jmap_executable=str(jmap_tool.get_jmap_package_path()),
        game_pid=game_pid,
        output_jmap_location=output
    )

    main_logic.close_game()


@dump.command(
    name="script_objects",
    help="Dumps the script objects from the game in the provided settings json.",
    short_help="Dumps the script objects from the game in the provided settings json.",
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
@click.option(
    "--jmap_path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        path_type=pathlib.Path,
    ),
    default=os.path.normpath(f'{os.getcwd()}/Modding/output.jmap'),
    help="Path to the a jmap file dumped from the game in the provided settings JSON file",
)
@click.option(
    "--output",
    default=os.path.normpath(f'{os.getcwd()}/Modding/output.utoc'),
    type=click.Path(resolve_path=True, path_type=pathlib.Path),
    help="The file location you want your utoc outputted to.",
)
def generate_script_objects(settings_json, jmap_path, output):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    retoc.ensure_retoc_is_installed()
    retoc.run_gen_script_objects_retoc_command(pathlib.Path(retoc.get_retoc_package_path()), jmap_path, output)
