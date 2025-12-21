@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli disable_mod command

uv run tempo_cli disable_mod --settings_json .tempo.json

exit /b
