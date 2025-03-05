from unreal_auto_mod import game_runner, packing, thread_game_monitor


def generate_mods(use_symlinks: bool):
    packing.cooking()
    packing.generate_mods(use_symlinks)
    game_runner.run_game()
    thread_game_monitor.game_monitor_thread()
