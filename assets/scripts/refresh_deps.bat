@echo off

cd /d "%~dp0"

cd ../..

uv lock --upgrade

uv sync

if exist ".pre-commit-config.yml" (
    uv run pre-commit autoupdate
) else if exist ".pre-commit-config.yaml" (
    uv run pre-commit autoupdate
)

exit /b