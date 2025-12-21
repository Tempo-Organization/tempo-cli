@echo off

cd /d "%~dp0"

cd ../..

uv venv

uv sync

if exist ".pre-commit-config.yml" (
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg
    uv run pre-commit install --hook-type pre-push
) else if exist ".pre-commit-config.yaml" (
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg
    uv run pre-commit install --hook-type pre-push
)

exit /b
