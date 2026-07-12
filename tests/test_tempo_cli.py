import sys
import time
import unittest
from collections.abc import Callable
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import click
from tempo_core import initialization, logger

from tempo_cli import main

# still need to add tests for the collection related commands


SETTINGS_FILE = (
    "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/.tempo.json"
)


@contextmanager
def temporary_argv(*args):  # noqa
    old_argv = sys.argv
    sys.argv = list(args)
    try:
        yield
    finally:
        sys.argv = old_argv


def init_tests() -> None:
    logger.log_message("started tempo core init")
    sys.argv.append("--config-file")
    sys.argv.append(str(SETTINGS_FILE))

    initialization.initialization()
    from tempo_cli.commands.tool import make_commands

    make_commands()


class TestTempo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_tests()

    @patch("tempo_cli.commands.clean.cleanup.callback")
    def test_clean_build_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "clean",
                "build",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.clean.cooked.callback")
    def test_clean_cooked_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "clean",
                "cooked",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.clean.full.callback")
    def test_clean_full_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "clean",
                "full",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.clean.resync_dir_with_repo.callback")
    def test_clean_resync_dir_with_repo_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "clean",
                "resync-dir-with-repo",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.dump.jmap.callback")
    def test_dump_jmap_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "dump",
                "jmap",
                "--config-file",
                SETTINGS_FILE,
                "--output",
                "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Content/DynamicClasses/output.jmap",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.dump.aes_keys.callback")
    def test_dump_aes_keys_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "dump",
                "aes-keys",
                "--config-file",
                SETTINGS_FILE,
                "--directory",
                "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding",
                "--dump-to-tempo-config",
                "True",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.dump.build_configuration.callback")
    def test_dump_build_configuration_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "dump",
                "build-configuration",
                "--config-file",
                SETTINGS_FILE,
                "--directory",
                "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding",
                "--dump-to-tempo-config",
                "True",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.dump.engine_version.callback")
    def test_dump_engine_version_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "dump",
                "engine-version",
                "--config-file",
                SETTINGS_FILE,
                "--directory",
                "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding",
                "--dump-to-tempo-config",
                "True",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.list.mods.callback")
    def test_list_mods_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "list",
                "mods",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.list.tools.callback")
    def test_list_tools_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "list",
                "tools",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.list.unreal_installs.callback")
    def test_list_unreal_installs_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "list",
                "unreal-installs",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.list.uplugins.callback")
    def test_list_uplugins_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "list",
                "uplugins",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    def test_tool_install_fmodel_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["fmodel"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "fmodel",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_umodel_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["umodel"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "umodel",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_injector_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["injector"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "injector",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_jmap_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["jmap"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "jmap",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_kismet_analyzer_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["kismet_analyzer"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "kismet_analyzer",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_patternsleuth_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["patternsleuth"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "patternsleuth",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_repak_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["repak"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "repak",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_retoc_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["retoc"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "retoc",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_spaghetti_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["spaghetti"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "spaghetti",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_stove_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["stove"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "stove",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_tempo_shell_scripts_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["tempo_shell_scripts"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "tempo_shell_scripts",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_uasset_gui_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["uasset_gui"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "uasset_gui",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    def test_tool_install_ue_vr_command(self) -> None:
        from tempo_cli.commands.tool import install

        command = install.commands["ue_vr"]

        with patch.object(command, "callback") as mock_command:
            with (
                temporary_argv(
                    "tempo_cli",
                    "tool",
                    "install",
                    "ue_vr",
                ),
                self.assertRaises(SystemExit) as context,
            ):
                main.main()

        self.assertEqual(context.exception.code, 0)
        mock_command.assert_called_once()

    @patch("tempo_cli.commands.uproject.build.callback")
    def test_uproject_build_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "uproject",
                "build",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uproject.cook.callback")
    def test_uproject_cook_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "uproject",
                "cook",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uproject.package.callback")
    def test_uproject_package_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "uproject",
                "package",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch(
        "tempo_cli.commands.uproject.resave_packages_and_fix_up_redirectors.callback"
    )
    def test_uproject_resave_packages_and_fix_up_redirectors_command(
        self, mock_command: MagicMock
    ) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "uproject",
                "resave-packages-and-fix-up-redirectors",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uproject.generate.callback")
    def test_uproject_generate_command(self, mock_command: MagicMock) -> None:
        uproject_file_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/testing.uproject"
        )
        if uproject_file_path.is_file():
            uproject_file_path.unlink()
        uproject_file_path.parent.mkdir(exist_ok=True)
        with (
            temporary_argv(
                "tempo_cli",
                "uproject",
                "generate",
                "--engine-major-association",
                "4",
                "--engine-minor-association",
                "27",
                "--category",
                "ThisIsACategory",
                "--description",
                "This is a description",
                str(uproject_file_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uplugin.generate.callback")
    def test_uplugin_generate_command(self, mock_command: MagicMock) -> None:
        uplugin_directory = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Plugins"
        )
        uplugin_name = "testing_uplugin_name"
        with (
            temporary_argv(
                "tempo_cli",
                "uplugin",
                "generate",
                "--can-contain-content",
                "True",
                str(uplugin_directory),
                uplugin_name,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uplugin.build.callback")
    def test_uplugin_build_command(self, mock_command: MagicMock) -> None:
        uplugin_directory = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Plugins"
        )
        uplugin_name = "testing_uplugin_name"
        with (
            temporary_argv(
                "tempo_cli",
                "uplugin",
                "generate",
                "--can-contain-content",
                "True",
                str(uplugin_directory),
                uplugin_name,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

        uplugin_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Plugins/testing_uplugin_name/testing_uplugin_name.uplugin"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "uplugin",
                "build",
                "--config-file",
                SETTINGS_FILE,
                "--uplugin-paths",
                str(uplugin_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.uplugin.remove.callback")
    def test_uplugin_remove_command(self, mock_command: MagicMock) -> None:
        uplugin_directory = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Plugins"
        )
        uplugin_name = "testing_uplugin_name"
        with (
            temporary_argv(
                "tempo_cli",
                "uplugin",
                "generate",
                "--can-contain-content",
                "True",
                str(uplugin_directory),
                uplugin_name,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

        uplugin_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Plugins/testing_uplugin_name/testing_uplugin_name.uplugin"
        )

        with (
            temporary_argv(
                "tempo_cli",
                "uplugin",
                "remove",
                "--uplugin-paths",
                str(uplugin_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.toml.add.callback")
    def test_toml_add_command(self, mock_command: MagicMock) -> None:
        toml_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.toml"
        )
        toml_path.touch()
        with (
            temporary_argv(
                "tempo_cli",
                "toml",
                "add",
                "--toml-path",
                str(toml_path),
                "--key",
                "key",
                "--value",
                "value",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.toml.remove.callback")
    def test_toml_remove_command(self, mock_command: MagicMock) -> None:
        toml_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.toml"
        )
        toml_path.touch()
        with (
            temporary_argv(
                "tempo_cli",
                "toml",
                "add",
                "--toml-path",
                str(toml_path),
                "--key",
                "key",
                "--value",
                "value",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

        with (
            temporary_argv(
                "tempo_cli",
                "toml",
                "remove",
                "--toml-path",
                str(toml_path),
                "--key",
                "key",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.json.add.callback")
    def test_json_add_command(self, mock_command: MagicMock) -> None:
        from tempo_core import file_io

        json_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.json"
        )
        json_path.unlink()
        json_path.touch()
        file_io.add_line_to_config(json_path, "{}")
        with (
            temporary_argv(
                "tempo_cli",
                "json",
                "add",
                "--json-path",
                str(json_path),
                "--key",
                "key",
                "--value",
                "value",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.json.remove.callback")
    def test_json_remove_command(self, mock_command: MagicMock) -> None:
        from tempo_core import file_io

        json_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.json"
        )
        json_path.unlink()
        json_path.touch()
        file_io.add_line_to_config(json_path, "{}")
        with (
            temporary_argv(
                "tempo_cli",
                "json",
                "add",
                "--json-path",
                str(json_path),
                "--key",
                "key",
                "--value",
                "value",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

        with (
            temporary_argv(
                "tempo_cli",
                "json",
                "remove",
                "--json-path",
                str(json_path),
                "--key",
                "key",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.close.game.callback")
    def test_close_game_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "close",
                "game",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.close.engine.callback")
    def test_close_engine_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "close",
                "engine",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.close.programs.callback")
    def test_close_programs_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "close",
                "programs",
                "--exe-names",
                "test.exe",
                "--exe-names",
                "test_2.exe",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.init.init.callback")
    def test_close_programs_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "init",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch(
        "tempo_cli.commands.ini.add_meta_data_tags_for_asset_registry_to_unreal_ini.callback"
    )
    def test_add_meta_data_tags_for_asset_registry_to_unreal_ini_command(
        self, mock_command: MagicMock
    ) -> None:
        ini_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Config/DefaultGame.ini"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "ini",
                "add-meta-data-tags-for-asset-registry-to-unreal-ini",
                "--ini-path",
                str(ini_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch(
        "tempo_cli.commands.ini.remove_meta_data_tags_for_asset_registry_from_unreal_ini.callback"
    )
    def test_remove_meta_data_tags_for_asset_registry_from_unreal_ini_command(
        self, mock_command: MagicMock
    ) -> None:
        ini_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Config/DefaultGame.ini"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "ini",
                "remove-meta-data-tags-for-asset-registry-from-unreal-ini",
                "--ini-path",
                str(ini_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.run.test_mods.callback")
    def test_run_test_mods_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "test-mods",
                "--config-file",
                SETTINGS_FILE,
                "--mod-names",
                "test_mod_name",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.run.test_mods_all.callback")
    def test_run_test_mods_all_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "test-mods-all",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.run.full_run.callback")
    def test_run_full_run_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "full-run",
                "--config-file",
                SETTINGS_FILE,
                "--mod-names",
                "test_mod_name",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)

    @patch("tempo_cli.commands.run.full_run_all.callback")
    def test_run_full_run_all_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "full-run-all",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.add_module_to_descriptor.callback")
    def test_run_add_module_to_descriptor_command(
        self, mock_command: MagicMock
    ) -> None:
        uproject_file_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject"
        )
        module_name = "test_module_name"
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "add-module-to-descriptor",
                "--host-type",
                "runtime",
                "--loading-phase",
                "earliest_possible",
                str(uproject_file_path),
                module_name,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.remove_modules_from_descriptor.callback")
    def test_run_remove_modules_from_descriptor_command(
        self, mock_command: MagicMock
    ) -> None:
        uproject_file_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject"
        )
        module_name = "test_module_name"
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "remove-modules-from-descriptor",
                "--module-names",
                module_name,
                str(uproject_file_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.engine.callback")
    def test_run_engine_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "engine",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.game.callback")
    def test_run_game_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "game",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.install_ue4ss.callback")
    def test_run_install_ue4ss_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "install-ue4ss",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.kismet_analyze_directory.callback")
    def test_run_kismet_analyze_directory_command(
        self, mock_command: MagicMock
    ) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "kismet-analyze-directory",
                "--config-file",
                SETTINGS_FILE,
                "--assets",
                "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.add_plugin_to_descriptor.callback")
    def test_run_add_plugin_to_descriptor_command(
        self, mock_command: MagicMock
    ) -> None:
        descriptor_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject"
        )
        plugin_name = "testing_uplugin_name"
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "add-plugin-to-descriptor",
                "--is-enabled",
                "True",
                str(descriptor_file),
                plugin_name,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.run.remove_plugins_from_descriptor.callback")
    def test_run_remove_plugins_from_descriptor_command(
        self, mock_command: MagicMock
    ) -> None:
        descriptor_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject"
        )
        plugin_name = "testing_uplugin_name"
        with (
            temporary_argv(
                "tempo_cli",
                "run",
                "remove-plugins-from-descriptor",
                "--plugin-names",
                plugin_name,
                str(descriptor_file),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.copy.callback")
    def test_file_io_copy_command(self, mock_command: MagicMock) -> None:
        descriptor_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject"
        )
        descriptor_file_2 = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/EscapeTheBackrooms.uproject.bak"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "copy",
                "--input-path",
                descriptor_file,
                "--output-path",
                descriptor_file_2,
                "--overwrite",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.delete.callback")
    def test_file_io_delete_command(self, mock_command: MagicMock) -> None:
        test_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.txt"
        )
        test_file.touch()
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "delete",
                "--input-paths",
                test_file,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.zip_directory_tree.callback")
    def test_file_io_zip_command(self, mock_command: MagicMock) -> None:
        test_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding"
        )
        test_output = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.zip"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "zip",
                "--directory",
                test_path,
                "--zip",
                test_output,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.unzip.callback")
    def test_file_io_unzip_command(self, mock_command: MagicMock) -> None:
        output_path_for_zip = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/zip_output"
        )
        test_zip = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.zip"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "unzip",
                "--output-directory",
                output_path_for_zip,
                "--zip",
                test_zip,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.symlink.callback")
    def test_file_io_symlink_command(self, mock_command: MagicMock) -> None:
        test_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.txt"
        )
        test_file.touch()
        test_file_2 = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test_2.txt"
        )
        if test_file_2.is_file():
            test_file_2.unlink()
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "symlink",
                "--input-path",
                str(test_file),
                "--output-path",
                str(test_file_2),
                "--overwrite",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.open_latest_log.callback")
    def test_file_io_open_latest_log_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "open-latest-log",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.move.callback")
    def test_file_io_move_command(self, mock_command: MagicMock) -> None:
        test_file = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test.txt"
        )
        test_file.touch()
        test_file_2 = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/test_2.txt"
        )
        if test_file_2.is_file():
            test_file_2.unlink()
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "move",
                "--input-path",
                str(test_file),
                "--output-path",
                str(test_file_2),
                "--overwrite",
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.generate_file_list.callback")
    def test_file_io_generate_file_list_command(self, mock_command: MagicMock) -> None:
        file_list_path = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/file_list.json"
        )
        dir_tree_to_make_file_list_of = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "generate-file-list",
                str(dir_tree_to_make_file_list_of),
                str(file_list_path),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.file_io.generate_game_file_list_json.callback")
    def test_file_io_generate_game_file_list_json_command(self, mock_command: MagicMock) -> None:
        output_json = Path(
            "C:/Users/mythi/OneDrive/Documents/GitHub/etb_mod_loader_uproject/Modding/output/game_file_list.json"
        )
        with (
            temporary_argv(
                "tempo_cli",
                "file-io",
                "generate-game-file-list-json",
                "--config-file",
                SETTINGS_FILE,
                "--output-json",
                str(output_json),
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.add_mod.callback")
    def test_mod_add_mod_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "add-mod",
                "--config-file",
                SETTINGS_FILE,
                '--mod-name',
                'example_mod_name',
                '--pak-dir-structure',
                '~mods',
                '--packing-type',
                'engine',
                '--mod-name-dir-type',
                'Mods',
                '--mod-name-dir-name-override',
                'example_mod_name_dir_name_override',
                '--pak-chunk-num',
                '100',
                '--compression-type',
                'None',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.remove_mod.callback")
    def test_mod_remove_mod_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "remove-mod",
                "--config-file",
                SETTINGS_FILE,
                '--mod-name',
                'example_mod_name',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.enable_mod.callback")
    def test_mod_enable_mod_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "enable-mod",
                "--config-file",
                SETTINGS_FILE,
                '--mod-name',
                'example_mod_name',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.enable_mods.callback")
    def test_mod_enable_mods_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "enable-mods",
                "--config-file",
                SETTINGS_FILE,
                '--mod-names',
                'example_mod_name',
                '--mod-names',
                'example_mod_name_2',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.disable_mod.callback")
    def test_mod_disable_mod_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "disable-mod",
                "--config-file",
                SETTINGS_FILE,
                '--mod-name',
                'example_mod_name',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.disable_mods.callback")
    def test_mod_disable_mods_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "disable-mods",
                "--config-file",
                SETTINGS_FILE,
                '--mod-names',
                'example_mod_name',
                '--mod-names',
                'example_mod_name_2',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.generate_mods.callback")
    def test_mod_generate_mods_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "generate-mods",
                "--config-file",
                SETTINGS_FILE,
                '--mod-names',
                'example_mod_name',
                '--mod-names',
                'example_mod_name_2',
                '--use-symlinks',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.generate_mods_all.callback")
    def test_mod_generate_mods_all_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "generate-mods-all",
                "--config-file",
                SETTINGS_FILE,
                '--use-symlinks',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.generate_mod_releases.callback")
    def test_mod_generate_mod_releases_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "generate-mod-releases",
                "--config-file",
                SETTINGS_FILE,
                '--mod-names',
                'example_mod_name_one',
                '--mod-names',
                '--example_mod_name_two',
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)


    @patch("tempo_cli.commands.mod.generate_mod_releases_all.callback")
    def test_mod_generate_mod_releases_all_command(self, mock_command: MagicMock) -> None:
        with (
            temporary_argv(
                "tempo_cli",
                "mod",
                "generate-mod-releases-all",
                "--config-file",
                SETTINGS_FILE,
            ),
            self.assertRaises(SystemExit) as context,
        ):
            main.main()
        self.assertEqual(context.exception.code, 0)
