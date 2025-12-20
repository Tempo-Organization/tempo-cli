@echo off

cd /d "%~dp0"

cd ../..

tempo_cli build --settings_json .tempo.json

exit /b