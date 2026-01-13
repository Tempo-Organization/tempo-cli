<h1 id="title" align="left">tempo-cli</h1>

Easy To Use Command Line Modding Utility For Unreal Engine Games 4.0-5.7  
Automates creation, and placement, of mod archives, and other various actions.  
For an in editor menu version check out [TempoInEditor](https://github.com/Tempo-Organization/TempoInEditor)  
For an in desktop or web version check out [tempo-gui](https://github.com/Tempo-Organization/tempo-gui)

<h2>Project Example:</h2>

[![Project Screenshot](https://github.com/Mythical-Github/UnrealAutoMod/assets/4b65e3a3-ae7f-4881-bea4-e73191594587.png)](https://github.com/user-attachments/assets/b491282c-59b8-47ae-a689-41d346d2a65c)


<h2 id="features">💪 Features</h2>

* Supports Unreal Engine versions: 4.0-5.7
* Supports loose file modding (unreal assets, not in a mod archive, like a .pak)
* Supports modding iostore games
* Automatic mod creation and placement
* Automatic engine cooking, and packaging
* Automatic game running
* Automatic editor running
* Event management system
* Process management events
* Window management events
* Automatic script/exec running events
* Supports creation of mod archives, through unreal_pak, repak, and engine made archives
* Ability to add launch params to various script/exec running
* Supports games with alternative packing structures (example game: Kingdom Hearts 3)
* Supports packing edited files, through the persistent_files dir, or through the Event Management System
* Easily configure what files end up in your final mod(s) and how with the Mod list within the config
* Supports loading from json file, so you can have multiple projects easily
* Logging
* Colorful printouts
* Ability to run in the background, with no windows
* And more...

# Installation

Install **tempo-core** first, then **tempo-cli**.

---

## tempo-core
```bash
# With pip.
pip install git+https://www.github.com/tempo-core@unit_testing
```

```bash
# Or pipx.
pipx install git+https://www.github.com/tempo-core@unit_testing
```

```bash
# Or uv.
uv add git+https://www.github.com/tempo-core@unit_testing
```

## tempo-cli
```bash
# With pip.
pip install git+https://www.github.com/tempo-cli@unit_testing
```

```bash
# Or pipx.
pipx install git+https://www.github.com/tempo-cli@unit_testing
```

```bash
# Or uv.
uv add git+https://www.github.com/tempo-cli@unit_testing
```

## Documentation

tempo-cli's documentation is available at [tempo-organization.github.io/tempo-cli](https://tempo-organization.github.io/tempo-cli/).

Additionally, the command line reference documentation can be viewed with `tempo_cli --help`.

## Bug Reports
If you encounter a bug or issue, please submit a report on the [issues page](https://github.com/Tempo-Organization/tempo-cli/issues). 
When creating an issue, please provide as much information as possible, including:
- Steps to reproduce the issue
- What you expect to happen, versus what is happening
- Any error messages or logs
- Your system operating system

## Contributing
Contributions are always appreciated, but please keep in mind the following:
- Before coding new features, try to make an issue to see if the idea/implementation needs any tweaking, or is out of scope
- Make sure your changes pass all pre-commit checks

## FAQ

#### What platforms does tempo-cli support?

Currently we support Windows and Linux.

#### As a game developer, can I use this for my game's mod support?

Yes, the license fully allows this, and we would love to see it.

## Acknowledgements

tempo-cli relies on these tools from the community to provide it's full functionality.

- **[Jmap](https://github.com/trumank/jmap)** - Unreal Engine reflection data format and extractor
- **[Repak](https://github.com/trumank/repak)** - Unreal Engine .pak file library and CLI in rust
- **[Retoc](https://github.com/trumank/retoc)** - Unreal Engine IoStore CLI packing/unpacking tool
- **[UE4SS](https://github.com/UE4SS-RE/RE-UE4SS)** - Injectable LUA scripting system, SDK generator, live property editor and other dumping utilities for UE4/5 games
- **[Patternsleuth](https://github.com/trumank/patternsleuth)** - Unreal Engine address scanner and test suite
- **[Umodel](https://www.gildor.org/en/projects/umodel)** - Viewer and exporter for Unreal Engine 1-4 assets (UE Viewer)
- **[Stove](https://github.com/bananaturtlesandwich/stove)** - an editor for cooked unreal engine 4/5 maps
- **[Spaghetti](https://github.com/bananaturtlesandwich/spaghetti)** - a function hooker for cooked unreal engine blueprints
- **[Fmodel](https://fmodel.app/)** - Unreal Engine Archives Explorer
- **[Kismet Analyzer](https://github.com/trumank/kismet-analyzer)** - Unreal Engine blueprint/kismet script reverse engineering and modding utilities
- **[UAssetGUI](https://github.com/atenfyr/UAssetGUI)** - A tool designed for low-level examination and modification of Unreal Engine game assets by hand
- **[Suzie](https://github.com/trumank/suzie)** - Unreal Engine Editor runtime class generation from dumped game reflection data

## License

tempo-cli is licensed under

- GNU General Public License version 3 ([LICENSE](LICENSE) or <https://opensource.org/license/gpl-3-0>)

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in tempo-cli
by you, as defined in the GNU General Public License version 3, shall be licensed as above, without any
additional terms or conditions.

[![license](https://www.gnu.org/graphics/gplv3-with-text-136x68.png)](LICENSE)
