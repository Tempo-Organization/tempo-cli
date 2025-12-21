@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli enable_mods command

SET /P mod_name=What is the name of the mod to enable? 

uv run tempo_cli enable_mods --settings_json .tempo.json --mod_names "%mod_name%"

exit /b
