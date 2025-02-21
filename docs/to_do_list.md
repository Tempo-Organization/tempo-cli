# UnrealAutoMod To-Do List


## To Do:
- [ ] tui bugging
- [ ] Switch to `pathlib` from strings
- [ ] fix logging not fully etending to end for color background
- [ ] think more about what to do with concurrent instances running/logs with them
- [ ] cleanup settings, remove global vars, only load from one place when accessing a setting from the json, add toml support
- [ ] recheck over symlink logic, make sure everywhere uses it where it should
- [ ] clean up hook states, and add any missing states
- [ ] sig logic, should copy existing and create if not exist on file placement option, or show warning


## Expanded Tokens:
- [ ] expanded tokens for configuration, maybe regex, 
        references:
                https://code.visualstudio.com/docs/editor/variables-reference, 
                https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes


## File Includes:
- [ ] make file include system more robust, 
- [ ] file include collections, toggleable auto include by name convention, with manual specification by name or path list
- [ ] file include has, file, dir, tree, maybe also regex possibilities from expanded tokens


## Iostore:
- [ ] non engine iostore, file_extemsions for iostore
- [ ] iostore repackaging more testing, ubulk stuff, try newer unreal engine versions
- [ ] finish iostore manual repackaging logic, check the following commands:
        full run
        full run all
        test mods
        test mods all
        generate mods
        generate mods all


## Hot Keys To Make:
- [ ] General Hotkey functionality
- [ ] Close game hotkey
- [ ] Run script again hotkey
- [ ] Bring Unreal Engine to front hotkey
- [ ] Bring game to front hotkey
- [ ] Close all hotkey (game, engine, and instances of UAM)


## Documentation:
- [ ] documentation github pages styling
- [ ] update feature list in docs


## Sooner Later:
- [ ] localization support


## Later Later:
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
- [ ] toml config support on top of keeping json
- [ ] diff game and file list, and backup diff, so later on can cleanup game list and restore from backup
- [ ] cli help replies and such are not colorized like the rest of the program, fix this
- [ ] Engine pak making compression variants (different types, in one run), defaults to compressed currently, can only do one type in one run right now


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
