@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli cleanup_build --settings_json .tempo.json

exit /b