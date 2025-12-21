@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli add_mod --settings_json .tempo.json

exit /b
