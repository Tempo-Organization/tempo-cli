@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli enable_mod command 

uv run tempo_cli enable_mods --settings_json .tempo.json

exit /b
