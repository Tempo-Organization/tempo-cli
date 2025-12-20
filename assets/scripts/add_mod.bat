@echo off

cd /d "%~dp0"

cd ../..

echo Running tempo_cli add_mod command

echo What is your mod name?
SET /P mod_name=

echo What is your pak dir structure? If pak_dir_structure is empty, set default to ~mods.
SET /P pak_dir_structure=

REM If pak_dir_structure is empty, set default to ~mods
if "%pak_dir_structure%"=="" (
    set "pak_dir_structure=~mods"
)

tempo_cli add_mod --settings_json .tempo.json "%mod_name%" "%pak_dir_structure%"

exit /b
