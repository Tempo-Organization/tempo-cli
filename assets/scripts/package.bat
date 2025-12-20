@echo off

cd /d "%~dp0"

cd ../..

tempo_cli package --settings_json .tempo.json

exit /b