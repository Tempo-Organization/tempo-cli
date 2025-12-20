@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli remove_mod command

SET /P mod_name=What is the name of the mod to remove? 

tempo_cli remove_mods --settings_json .tempo.json --mod_names "%mod_name%"

exit /b
