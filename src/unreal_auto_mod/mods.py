from unreal_auto_mod import game_runner, packing
from unreal_auto_mod.threads import game_monitor


def generate_mods(use_symlinks: bool):
    packing.cooking()
    packing.generate_mods(use_symlinks)
    game_runner.run_game()
    game_monitor.game_monitor_thread()
