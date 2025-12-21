@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli open_latest_log --settings_json .tempo.json

exit /b