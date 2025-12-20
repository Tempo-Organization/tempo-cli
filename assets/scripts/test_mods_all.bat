@echo off

cd /d "%~dp0"

cd ../..

tempo_cli test_mods_all --settings_json .tempo.json

rem tempo_cli test_mods_all --settings_json .tempo.json --toggle_engine

exit /b