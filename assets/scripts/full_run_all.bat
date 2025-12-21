@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli full_run_all --settings_json .tempo.json

exit /b