# FModel

FModel is an Unreal Engine asset viewer and explorer. It requires some game-specific configuration before it can properly load a game's assets.

### Manual Installation

Download FModel from the [official releases page](https://github.com/4sval/FModel/releases), and extract it to your location of choice.

### Installing with Tempo

FModel can also be installed using `tempo_cli`:

```console
tempo_cli tool install fmodel
```

To install FModel and immediately launch it:

```console
tempo_cli tool install fmodel --run-after-install
```

To run FModel, and automatically download if not installed:

```console
tempo_cli tool run fmodel
```

## Configuring FModel

FModel often needs a few things to be able to open, extract, and parse information in assets.

The most common configuration options are:

| Setting | Required | Description |
|---|:---:|---|
| **Unreal Engine Version** | Always | The Unreal Engine version used by the game, there are game specific presets, not every game has one |
| **`.usmap` File** | Sometimes | Property mappings required by some games |
| **AES Key** | Sometimes | Used to decrypt encrypted game assets |

### Unreal Engine Version

FModel requires the Unreal Engine version used by the game.

For example:

```text
Unreal Engine 4.27
```

or:

```text
Unreal Engine 5.3
```

add a section here on how to determine a game's unreal engine version

### `.usmap` Files

Some games require a `.usmap` file to correctly interpret their assets.

explain how to get a usmap file, and how to configure fmodel to use the usmap file as well
explain how to tell if one is even needed

### AES Keys

Depending on the game, FModel may need one or more AES keys.
Most games that require AES keys only need a single key.
AES keys are game-specific. The correct key must be used for the version of the game you are trying to load.

explain how to get one or more aes keys from the game

## Quick Setup

For a typical game, the setup process is:

1. **Install FModel**
2. **Select the game's directory**
3. **Select the correct Unreal Engine version or game specific preset if one exists**
5. **Add a `.usmap` file if required**
6. **Add the required AES key(s) if necessary**
7. **Load one or more archives via the load section in FModel**