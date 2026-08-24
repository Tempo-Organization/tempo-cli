# Settings

Tempo stores its configuration as a JSON object. Settings are grouped into sections based on the part of Tempo they control.

> **Note:** Not every setting is required. Many settings can be inferred automatically from other configuration values, environment variables, or detected Unreal Engine information.

## Configuration Structure

- [`mods_info`](#mods-info)
- [`game_info`](#game-info)
- [`engine_info`](#engine-info)
- [`process_kill_events`](#process-kill-events)
- [`window_management_events`](#window-management-events)
- [`exec_events`](#exec-events)
- [`git_info`](#git-info)
- [`repak_info`](#repak-info)
- [`cache`](#cache)
- [`packaging_uproject_name`](#packaging-uproject-name)
- [`optionals`](#optionals)

---

## Mods Info

`mods_info` contains the configuration for each mod.

```json
{
    "mods_info": {
        "ExampleMod": {
            "persistent_files_directory": "C:/Path/To/Persistent/Files/Directory",
            "auto_include_mod_name_dir_name": true,
            "packing_type": "unreal_pak",
            "pak_chunk_num": 1,
            "sig_method_type": "copy",
            "is_enabled": true,
            "pak_dir_structure": "~mods",
            "compression_type": "Zlib",
            "mod_name_dir_type": "Mods",
            "mod_name_dir_name_override": "ExampleModNameDirNameOverride",
            "file_includes": {
                "asset_paths": [
                    "Content/Mods/Folder/AssetName",
                    "Content/Mods/Folder/AssetNameTwo"
                ],
                "tree_paths": [
                    "Content/Mods/FolderTwo",
                    "Content/GameModes/GunGame"
                ]
            }
        },
        "AnotherMod": {
            "persistent_files_directory": "C:/Path/To/Another/Persistent/Files/Directory",
            "auto_include_mod_name_dir_name": false,
            "packing_type": "engine",
            "pak_chunk_num": 2,
            "sig_method_type": "none",
            "is_enabled": true,
            "pak_dir_structure": "~mods",
            "compression_type": "Oodle",
            "mod_name_dir_type": "Mods",
            "mod_name_dir_name_override": "AnotherModNameDir",
            "file_includes": {
                "asset_paths": [
                    "Content/AnotherMod/AssetOne",
                    "Content/AnotherMod/AssetTwo"
                ],
                "tree_paths": [
                    "Content/AnotherMod",
                    "Content/Weapons"
                ]
            }
        }
    }
}
```

### General Mod Settings

| Setting | Description |
|---|---|
| `mod_name` | Name of the mod. |
| `persistent_files_directory` | Directory containing files that should persist between operations, useful for edited cooked assets, and inis. |
| `auto_include_mod_name_dir_name` | Automatically includes the files in the at Content/ModNameDirType/ModName tree in various operations, defaults to true. |
| [`packing_type`](../../reference/api/index.md#tempo_core.data_structures.PackingType) | Determines the type of package produced for the mod. |
| `pak_chunk_num` | Chunk number used when creating the pak. |
| [`sig_method_type`](../../reference/api/index.md#tempo_core.data_structures.SigMethodType) | Signature method used for the generated package. |
| `is_enabled` | Determines whether the mod is enabled, if not specified, defaults to true. |
| `pak_dir_structure` | Determines the directory structure used to place the mod files in your game's Paks directory, and for releases. |
| [`compression_type`](../../reference/api/index.md#tempo_core.data_structures.CompressionType) | Compression method used when packaging the mod. |
| `mod_name_dir_type` | What foldername to automatically include files for, often is Mods, or CustomContent. |
| `mod_name_dir_name_override` | Overrides the automatically generated mod-name directory. Can be useful for internally having a nice folder name, while having a _P in your final file name. |
| `file_includes.asset_paths` | Individual Unreal asset paths to include. |
| `file_includes.tree_paths` | Paths to directory trees where all files with be included. |

---

## Game Info

`game_info` describes the game that Tempo is managing.

```json
{
    "game_info": {
        "game_exe_path": "C:/Games/Example/Game.exe",
        "game_launcher_exe": "C:/Programs/Steam/Steam.exe",
        "window_title_override": "Example Game",
        "launch_type": "steam",
        "game_id": "123456",
        "launch_params": [
            "--param_one",
            "--param_two"
        ],
        "is_iostore": false
    }
}
```

### Settings

| Setting | Description |
|---|---|
| `game_exe_path` | Path to the game's executable. |
| `game_launcher_exe` | Optional launcher executable used to start the game. |
| `window_title_override` | Overrides the window title used when identifying the game window. |
| [`launch_type`](../../reference/api/index.md#tempo_core.data_structures.GameLaunchType) | Determines how the game is launched. Usually, through steam, or directly through the executable.|
| `game_id` | Game id for the game, often the steam app id. |
| `launch_params` | Additional parameters passed when launching the game. |
| `is_iostore` | Indicates whether the game uses Unreal Engine's IoStore packaging system, usually automatically determined. |

---

## Engine Info

`engine_info` contains Unreal Engine and project configuration.

```json
{
    "engine_info": {
        "unreal_engine_dir": "D:/UnrealEngine/UE_5.7",
        "unreal_project_file": "C:/Projects/Game/Game.uproject",
        "engine_building_args": [],
        "engine_packaging_args": [],
        "engine_cooking_args": [],
        "engine_launch_args": [],
        "build_type": "Shipping",
        "unreal_engine_major_version": 5,
        "unreal_engine_minor_version": 7,
        "build_target_platform": "Win64",
        "unreal_engine_target_platform": "WindowsNoEditor"
    }
}
```

### Settings

| Setting | Description |
|---|---|
| `unreal_engine_dir` | Path to the Unreal Engine installation. |
| `unreal_project_file` | Path to the Unreal Engine `.uproject` file. |
| `engine_building_args` | Override the default arguments used when building the Unreal project. |
| `engine_packaging_args` | Override the default arguments used when packaging the project. |
| `engine_cooking_args` | Override the default arguments used when cooking the project. |
| `engine_launch_args` | Override the default arguments used when launching the project or game. |
| [`build_type`](../../reference/api/index.md#tempo_core.data_structures.unreal_engine_build_targets) | Determines the type of Unreal Engine build to perform. |
| `unreal_engine_major_version` | Unreal Engine major version, such as `4` or `5`. |
| `unreal_engine_minor_version` | Unreal Engine minor version, such as `27` or `7`. |
| `build_target_platform` | Platform targeted when building the project. |
| [`unreal_engine_target_platform`](../../reference/api/index.md#tempo_core.data_structures.unreal_engine_target_platforms) | Platform targeted by Unreal Engine operations. |

## Process Kill Events

`process_kill_events` controls processes that Tempo monitors for to terminate.

```json
{
    "process_kill_events": {
        "processes": [
            {
                "hook_state": "pre_game_launch",
                "use_substring_check": true,
                "process_name": "ExampleGame.exe"
            },
            {
                "hook_state": "post_game_launch",
                "use_substring_check": false,
                "process_name": "ExampleLauncher.exe"
            }
        ],
        "auto_close_game": true
    }
}
```

| Setting | Description |
|---|---|
| [`hook_state`](../../reference/api/index.md#tempo_core.data_structures.HookStateType) | Controls when this process management event will fire. |
| `use_substring_check` | Determines whether the process name is matched as a substring rather than exactly. |
| `process_name` | Name of the process to monitor. |
| `auto_close_game` | Controls whether Tempo automatically closes the game as needed for various file operations and testing. |

## Window Management Events

`window_management_events` Allows management of application windows through Tempo.

```json
{
    "window_management_events": [
        {
            "hook_state": "pre_game_launch",
            "use_substring_check": true,
            "window_name": "Example Game",
            "window_behaviour": {
                "position": {
                    "x": 0,
                    "y": 0
                },
                "resolution": {
                    "width": 1920,
                    "height": 1080
                }
            }
        },
        {
            "hook_state": "post_game_launch",
            "use_substring_check": false,
            "window_name": "Another Game",
            "window_behaviour": {
                "position": {
                    "x": 100,
                    "y": 100
                },
                "resolution": {
                    "width": 1280,
                    "height": 720
                }
            }
        }
    ]
}
```

### Settings

| Setting | Description |
|---|---|
| [`hook_state`](../../reference/api/index.md#tempo_core.data_structures.HookStateType) | Controls when this window management event will fire. |
| `use_substring_check` | Determines whether `window_name` is matched as a substring. |
| `window_name` | Name of the window to manage. |
| [`window_behaviour`](../../reference/api/index.md#tempo_core.data_structures.WindowAction) | Determines how the window should be managed. |
| `position.x` | Horizontal position of the window. |
| `position.y` | Vertical position of the window. |
| `resolution.width` | Width of the window. |
| `resolution.height` | Height of the window. |

---

## Exec Events

`exec_events` defines commands or executables that Tempo can launch.

```json
{
    "exec_events": [
        {
            "hook_state": "pre_game_launch",
            "alt_exe_path": "C:/Path/To/Executable.exe",
            "variable_args": [
                "--param_one",
                "--param_two"
            ],
            "execution_mode": "sync"
        },
        {
            "hook_state": "post_game_launch",
            "alt_exe_path": "C:/Path/To/AnotherExecutable.exe",
            "variable_args": [
                "--example",
                "--another_param"
            ],
            "execution_mode": "async"
        }
    ]
}
```

### Settings

| Setting | Description |
|---|---|
| [`hook_state`](../../reference/api/index.md#tempo_core.data_structures.HookStateType) | Controls when this execution management event will fire. |
| `alt_exe_path` | executable path. |
| `variable_args` | Arguments that can be supplied to run when executing the program. |
| [`execution_mode`](../../reference/api/index.md#tempo_core.data_structures.ExecutionMode) | Determines how the executable is launched. |

---

## Git Info

`git_info` contains Git repository configuration.

```json
{
    "git_info": {
        "repo_path": "C:/Projects/MyMod"
    }
}
```

| Setting | Description |
|---|---|
| `repo_path` | Path to the Git repository associated with the project. |

---

## Repak Info

`repak_info` controls the version and compression settings used by Repak.

```json
{
    "repak_info": {
        "repak_compression_type": "Zlib",
        "repak_version": "V4",
        "repak_pack_version": "v0.2.3"
    }
}
```

| Setting | Description |
|---|---|
| [`repak_compression_type`](../../reference/api/index.md#tempo_core.programs.repak.RepakCompressionType) | Compression method passed to Repak. |
| `repak_version` | Version of Repak to use. |
| `repak_pack_version` | Pak format version to generate. |

---

## Cache

`cache` controls Tempo's local cache.

```json
{
    "cache": {
        "cache_dir": "..."
    }
}
```

| Setting | Description |
|---|---|
| `cache_dir` | Directory where Tempo stores cached files and data. |

---

## Packaging Uproject Name

`packaging_uproject_name` controls the name used when packaging a project.

```json
{
    "packaging_uproject_name": {
        "name": "ExampleProject"
    }
}
```

| Setting | Description |
|---|---|
| `name` | Uproject name used during packaging. |

> **Note:** This setting is intended to be revisited. In the future, the name may be derived from [`engine_info`](#engine-info) or [`game_info`](#game-info).

---

## Optionals

`optionals` contains optional paths to external tools.

```json
{
    "optionals": {
        "ide_path": "C:/Program Files/IDE/IDE.exe",
        "blender_path": "C:/Program Files/Blender Foundation/Blender/blender.exe"
    }
}
```

| Setting | Description |
|---|---|
| `ide_path` | Path to the IDE used for development. |
| `blender_path` | Path to the Blender executable. |

These settings are optional and are only required when the corresponding tool is used by a workflow.

---

## Minimal Configuration

A minimal configuration does not necessarily need to specify every available setting.

For example:

```json
{
    "game_info": {
        "game_exe_path": "C:/Games/Example/Game.exe"
    },
    "engine_info": {
        "unreal_engine_dir": "D:/UnrealEngine/UE_5.7",
        "unreal_project_file": "C:/Projects/Example/Example.uproject"
    }
}
```

Tempo can derive additional information from these paths where possible.

## Configuration Precedence

In general, settings may be supplied through:

1. Command-line arguments
2. Environment variables
3. Environment files
4. Configuration files
5. Default values or automatically detected system information

The effective priority is:

**command line > environment variable > environment file > configuration > default/auto-detected**

> **Note:** Environment files are currently not supported.