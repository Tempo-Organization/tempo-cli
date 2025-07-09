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

setup: clean_up
  uv venv
  uv run pre-commit install
  uv run pre-commit install --hook-type commit-msg

build:
  uv run pyinstaller --noconfirm --onefile --hidden-import=textual.widgets._tab --console --name tempo_cli --collect-data trogon src/tempo_cli/__main__.py
  uv run pyinstaller --noconfirm --onefile --hidden-import=textual.widgets._tab --console --name tempo_cli_headless --collect-data trogon src/tempo_cli/__main__.pyw

run_exe:
  dist\tempo_cli.exe --help

build_run_exe: build run_exe

rebuild: clean_up build

rebuild_run_exe: clean_up build run_exe

alias clean := clean_up

clean_up:
  if (Test-Path ".venv") { Remove-Item ".venv" -Recurse -Force }
  git clean -d -X --force

alias cz_commit := commitizen_commit
alias commit := commitizen_commit

commitizen_commit:
  uv run cz commit

alias cz_commit_retry := commitizen_commit_retry
alias commit_retry := commitizen_commit_retry

commitizen_commit_retry:
  uv run cz commit --retry

switch_to_main_branch:
  git switch main

switch_to_dev_branch:
  git switch dev

git_push:
  git push

git_pull:
  git pull

mkdocs_build:
  mkdocs build

mkdocs_serve:
  mkdocs serve

git_add_all:
  git add .

git_reset:
  git reset

pre_commit_auto_update:
  uv run pre-commit autoupdate

pre_commit_check_all:
  uv run pre-commit run --all-files

git_create_stash:
  while ($true) { if (($pathToAdd = Read-Host "Enter a path to add or drag a file over this window (press Enter to exit)") -eq "") { Write-Host "Exiting..."; break }; if (($stashComment = Read-Host "Enter a comment/message for this stash") -eq "") { Write-Host "Stash comment cannot be empty. Please try again." -ForegroundColor Red; continue }; git stash push "$pathToAdd" -m "$stashComment"; Write-Host "`nStash created for '$pathToAdd' with comment: $stashComment`n" }

git_pop_stash:
  while ($true) { Clear-Host; Write-Host "Current git stashes:"; git stash list; Write-Host ""; $stashes = Read-Host "Enter stash index(es) to pop (space separated), or press Enter to exit"; if ([string]::IsNullOrWhiteSpace($stashes)) { Write-Host "Exiting..."; break }; foreach ($s in $stashes -split "\s+") { Write-Host "Popping stash $s..."; git stash pop "stash@{$s}"; Start-Sleep -Seconds 2; Clear-Host; Write-Host "After popping stash $s, remaining stashes:"; git stash list; Write-Host "" } }

git_add_files:
  while ($true) { $pathToAdd = Read-Host "Enter a path to add or drag a file over this window (press Enter to finish)"; if ([string]::IsNullOrWhiteSpace($pathToAdd)) { Write-Host "Done adding paths."; Pause; break }; git add "$pathToAdd"; Write-Host "Added `"$pathToAdd`"" }

refresh_deps: pre_commit_auto_update
  uv lock --upgrade

run:
  uv pip install -e .
  uv run tempo_cli --help
