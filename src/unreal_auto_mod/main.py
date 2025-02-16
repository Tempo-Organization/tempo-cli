from unreal_auto_mod import cli, initialization, log


def main():
    try:
        initialization.initialization()
        cli.cli()
    except Exception as error_message:
        log.log_message(str(error_message))
