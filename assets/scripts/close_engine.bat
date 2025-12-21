@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli close_engine --settings_json .tempo.json

exit /b