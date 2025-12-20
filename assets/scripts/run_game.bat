@echo off

cd /d "%~dp0"

cd ../..

tempo_cli run_game --settings_json .tempo.json

exit /b