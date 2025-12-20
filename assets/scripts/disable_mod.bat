@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli disable_mods command

SET /P mod_name=What is the name of the mod to disable? 

tempo_cli disable_mods --settings_json .tempo.json --mod_names "%mod_name%"

exit /b
