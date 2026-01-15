# Getting Started

All you need to get started making mods with Tempo.

## Requirements

Tempo runs on **Windows** and **Linux**.

- **[Git](https://git-scm.com/downloads)**
- **[uv](https://uv.io/)** (later on, uv will not be needed for prebuilt executables)
- **[Python 3.9.1 or later](https://www.python.org/downloads/)** is needed only if you install from **source** via pip or pipx.  
- For **prebuilt executables**, Python is **not required**, but Git and uv are still needed.



## Installation

Tempo is distributed as a single package, [tempo-cli](https://www.github.com/tempo-cli@unit_testing), which relies on [tempo-core](https://www.github.com/tempo-core@unit_testing).

### Install `tempo-cli'

=== "pip"

    ``` bash
    pip install git+https://www.github.com/tempo-cli@unit_testing
    ```

=== "pipx"

    ``` bash
    pipx install git+https://www.github.com/tempo-cli@unit_testing
    ```

=== "uv"

    ``` bash
    uv add git+https://www.github.com/tempo-cli@unit_testing
    ```

### Prebuilt Releases

If you prefer **prebuilt executables**, downloads are available for **Windows** and **Linux** in the [Releases section](https://github.com/Tempo-Organization/tempo-cli/releases):

- **Windows**: `tempo_cli.exe`  
- **Linux**: `tempo_cli`

#### Adding to your PATH

To run the prebuilt executables from any terminal, you should add them to your system PATH:

=== "Windows"
    **Windows:**
    
    1. Move `tempo_cli.exe` to a folder of your choice (e.g. `C:\programs\tempo_cli`).
    2. Open **Settings → System → About → Advanced system settings → Environment Variables**.
    3. Under **System Variables**, select `Path` and click **Edit**.
    4. Click **New** and add the folder path where `tempo_cli.exe` is located (e.g. `C:\programs\tempo_cli`).
    5. Click **OK** to save changes. Open a new Command Prompt to use `tempo_cli` from any directory.

=== "Linux"
    **Linux:**
    
    1. Move `tempo_cli` to a folder of your choice (e.g., `/usr/local/bin`).
    2. Make sure it’s executable:  
    
    ```bash
    chmod +x /usr/local/bin/tempo_cli
    ```
    
    3. If the folder isn’t already in your PATH, add it by editing your shell config file (`~/.bashrc`, `~/.zshrc`, etc.):
    
    ```bash
    export PATH=$PATH:/usr/local/bin
    ```
    
    4. Reload your shell:
    
    ```bash
    source ~/.bashrc
    ```
    
    You can now run `tempo_cli` from any directory.
    
    ### Tempo CLI
    
    There are a number of commands available which will aid you in building mods. Run the following for a list of the available commands:
    
    ```bash
    tempo_cli --help
    ```

## Need help?

See the [help](./help.md) page for how to get help with Tempo, or to report bugs.
