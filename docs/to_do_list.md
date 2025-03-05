# UnrealAutoMod To-Do List


## To Do:
- [ ] cleanup modules, no imports within functions, etc...


## File Includes:
- [ ] add each of the new collection commands to the launch json
- [ ] logic for mod making to scan collection contents

cli commands:
        - [ ] create collection
        - [ ] set color
        - [ ] rename collection
        - [ ] delete collection
        - [ ] disable collection
        - [ ] enable collection
        - [ ] set guid
        - [ ] set parent guid
        - [ ] set file version
        - [ ] set collection type
        - [ ] add content path
        - [ ] remove content path
        - [ ] add content paths
        - [ ] remove content paths
        - [ ] add collection to mod entry
        - [ ] remove collection from mod entry
        - [ ] add collections to mod entry
        - [ ] remove collections from mod entry


## Expanded Tokens:
- [ ] expanded tokens for configuration, works with env vars, up a directory, path seperator
        references:
                https://code.visualstudio.com/docs/editor/variables-reference, 
                https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes


## Iostore:
- [ ] recheck over symlink logic for create iostore mods, same with sig logic
- [ ] non engine iostore, file_extemsions for iostore
- [ ] iostore repackaging more testing, ubulk stuff, try newer unreal engine versions
- [ ] finish iostore manual repackaging logic, check the following commands:
        full run
        full run all
        test mods
        test mods all
        generate mods
        generate mods all


## Documentation:
- [ ] documentation github pages styling
- [ ] update feature list in docs


## Sooner Later:
- [ ] localization support


## Later Later:
- [ ] interactive wrappers
- [ ] overrideable colors, ability to disable coloring/progress bars/logging
- [ ] appease linter
- [ ] generate project files for uproject
- [ ] uproject, uplugin, engine ini edits, for popular things, maybe also generic
- [ ] generate uproject from win 64 exe, will need the unreal engine version
- [ ] Mod Conflict Checker
- [ ] unpack/repack game/mods
- [ ] list game/mod contents
- [ ] linux support
- [ ] retoc commands/functionality
- [ ] compatible game list, more for less techy people, since the tool works on virtually all games
- [ ] compile all blueprints commandlet usage, maybe somehow setup for any commandlets
- [ ] cli command for dumping usmapping
- [ ] cli command for getting unreal engine version
- [ ] cli command for getting aes key
- [ ] cli command for getting uproject name
- [ ] diff game and file list, and backup diff, so later on can cleanup game list and restore from backup
- [ ] cli help replies and such are not colorized like the rest of the program, fix this
- [ ] Engine pak making compression variants (different types, in one run), defaults to compressed currently, can only do one type in one run right now
- [ ] Switch to `pathlib` from strings
- [ ] add toml support
- [ ] layout support command


        ## Events to look into
        - [ ] move
        - [ ] copy
        - [ ] rename
        - [ ] symlink
        - [ ] delete
        - [ ] zip
        - [ ] unzip
        - [ ] add to json
        - [ ] remove from json
        - [ ] add to ini
        - [ ] remove from ini
        - [ ] add to toml
        - [ ] remove from toml
        - [ ] add to text file
        - [ ] remove from text file
        - [ ] git stuff
        - [ ] gen engine stuff
        - [ ] open game dir
        - [ ] open game paks dir
        - [ ] open mod releases dir
        - [ ] open dist dir
        - [ ] openm persistent mods dir
        - [ ] open unreal auto mod dir
        - [ ] open uproject dir


        ## Hot Keys To Make:
        - [ ] General Hotkey functionality
        - [ ] Close game hotkey
        - [ ] Run script again hotkey
        - [ ] Bring Unreal Engine to front hotkey
        - [ ] Bring game to front hotkey
        - [ ] Close all hotkey (game, engine, and instances of UAM)

automate asset import for meshes/skeletons/textures/physics assets, pal/da, etc.... and various properties
