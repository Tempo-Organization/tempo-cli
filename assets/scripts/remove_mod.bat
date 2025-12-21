@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli remove_mod --settings_json .tempo.json

exit /b
