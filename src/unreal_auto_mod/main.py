from unreal_auto_mod import cli, logger


def main():
    try:
        cli.cli()
    except Exception as error_message:
        logger.log_message(str(error_message))
