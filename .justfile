# Cross platform shebang:
shebang := if os() == 'windows' {
  'powershell.exe'
} else {
  '/usr/bin/env pwsh'
}

# Set shell for non-Windows OSs:
set shell := ["powershell", "-c"]

# Set shell for Windows OSs:
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# If you have PowerShell Core installed and want to use it,
# use `pwsh.exe` instead of `powershell.exe`


alias list := default

default:
  just --list

setup: clean
  uv venv
  uv run pre-commit install
  uv run pre-commit install --hook-type commit-msg
  uv run pre-commit install --hook-type pre-push

build:
  uv run pyinstaller --noconfirm --onefile --hidden-import=textual.widgets._tab --console --name tempo_cli --collect-data trogon src/tempo_cli/__main__.py

build_all:
  uv run pyinstaller --noconfirm --onefile --hidden-import=textual.widgets._tab --console --name tempo_cli --collect-data trogon src/tempo_cli/__main__.py
  uv run pyinstaller --noconfirm --onefile --hidden-import=textual.widgets._tab --console --name tempo_cli_headless --collect-data trogon src/tempo_cli/__main__.pyw

run_exe:
  dist\tempo_cli.exe --help

build_run_exe: build run_exe

rebuild: clean build

rebuild_run_exe: clean build run_exe

clean:
  git clean -d -X --force

commit:
  uv run cz commit

commit_retry:
  uv run cz commit --retry

docs_build:
  mkdocs build

docs_serve:
  mkdocs serve

refresh_deps:
  uv run pre-commit autoupdate
  uv lock --upgrade
  uv sync

run:
  uv run tempo_cli --help
