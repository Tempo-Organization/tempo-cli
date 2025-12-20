@echo off

cd /d "%~dp0"

cd ../..

tempo_cli full_run_all --settings_json .tempo.json

exit /b