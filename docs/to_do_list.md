---
hide:
  - navigation
---

## Main CLI Commands

- [ ] `cli command add to ini`
- [ ] `cli command remove from ini`
- [ ] `cli command add to text file`
- [ ] `cli command remove from text file`
- [ ] `cli command git stuff`
- [ ] `cli command gen engine stuff`
- [ ] `cli command open game dir`
- [ ] `cli command open game paks dir`
- [ ] `cli command open mod releases dir`
- [ ] `cli command open dist dir`
- [ ] `cli command open persistent mods dir`
- [ ] `cli command open unreal auto mod dir`
- [ ] `cli command open uproject dir`
- [ ] `cli command open provided dir`
- [ ] `cli command open provided file in default opener`

---

## File Operations

- [ ] Create empty text file
- [ ] Add new line to text file
- [ ] Remove from text file by start, end, contains, etc.
- [ ] Create new JSON file

---

## Installation / Setup

- [ ] Add to PATH upon install from install sources

---

## Later Later

- [ ] Overridable colors, ability to disable coloring/progress bars/logging
- [ ] Generate project files for uproject
- [ ] Uproject, uplugin, engine ini edits for popular things (maybe also generic)
- [ ] Default map change, game instance edits
- [ ] Generate uproject from Win64 EXE (requires Unreal Engine version)
- [ ] Unpack/repack game/mods
- [ ] List game/mod contents
- [ ] Logic for mod making to scan collection contents

---

## Later Later Later

- [ ] Automate installing from EGS
- [ ] Mod Conflict Checker
- [ ] Diff game and file list, backup diff (for cleanup/restore)
- [ ] Layout support command
- [ ] Engine pak making compression variants (defaults to compressed)
- [ ] Switch to `pathlib` from strings

---

## Asset Automation

- [ ] Automate asset import for meshes/skeletons/textures/physics assets, PAL/DA, etc.
- [ ] Handle various properties

---

## Hotkeys

- [ ] General hotkey functionality
- [ ] Close game hotkey
- [ ] Run script again hotkey
- [ ] Bring Unreal Engine to front hotkey
- [ ] Bring game to front hotkey
- [ ] Close all hotkey (game, engine, and instances of Tempo)

---

## Docs & Examples

- [ ] GitHub Actions example with zipping files
- [ ] Pre-commit example

---

## Configuration & Settings

- [ ] Expanded tokens for configuration (supports env vars, up a directory, path separator)  
  References:  
  - [VS Code Variables Reference](https://code.visualstudio.com/docs/editor/variables-reference)  
  - [VS Code Launch JSON Attributes](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)
- [ ] Fix it so all settings are loaded and saved from one place (currently several functions don’t follow this)
- [ ] Add TOML support

### Config Types

- Workspace config
- Project config
- Mod-specific config
- Game config
- Config versions


















auto detect mods and add to config (checks for common conventions and acts based on that) 
auto run self hosted actions runner
setup self hosted actions runner
setup for action runners


Commitizen supports explicitly specifying a configuration file using the --config option, which is useful when the configuration file is not located in the project root directory. When --config is provided, Commitizen will only load configuration from the specified file and will not search for configuration files using the default search order described above. If the specified configuration file does not exist, Commitizen raises the ConfigFileNotFound error. If the specified configuration file exists but is empty, Commitizen raises the ConfigFileIsEmpty error.
commitzen also has scopes for monorepo support when committing



project update
project commit
project push
project bump
project publish
project dep add
project dep remove
project dep refresh

mod update
mod commit
mod publish
mod bump
mod push
mod dep add
mod dep remove
mod dep refresh




dependency groups
version ranges
check uv/py_project.toml for inspo
