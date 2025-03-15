import os
import subprocess

from unreal_auto_mod import logger
from unreal_auto_mod.data_structures import ExecutionMode
from unreal_auto_mod.file_io import ensure_path_quoted


def run_app(
        exe_path: str,
        exec_mode: ExecutionMode = ExecutionMode.SYNC,
        args: list = [],
        working_dir: str = None
    ):

    exe_path = ensure_path_quoted(exe_path)

    if exec_mode == ExecutionMode.SYNC:
        command = exe_path
        for arg in args:
            command = f'{command} {arg}'
        logger.log_message('----------------------------------------------------')
        logger.log_message(f'Command: main executable: {exe_path}')
        for arg in args:
            logger.log_message(f'Command: arg: {arg}')
        logger.log_message('----------------------------------------------------')
        logger.log_message(f'Command: {command} running with the {exec_mode} enum')
        if working_dir:
            if os.path.isdir(working_dir):
                os.chdir(working_dir)

        process = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)

        for line in iter(process.stdout.readline, ''):
            logger.log_message(line.strip())

        process.stdout.close()
        process.wait()
        logger.log_message(f'Command: {command} finished')

    elif exec_mode == ExecutionMode.ASYNC:
        command = exe_path
        for arg in args:
            command = f'{command} {arg}'
        logger.log_message(f'Command: {command} started with the {exec_mode} enum')
        subprocess.Popen(command, cwd=working_dir, start_new_session=True, shell=True)
