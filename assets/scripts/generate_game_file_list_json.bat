@echo off

cd /d "%~dp0"

cd ../..

tempo_cli generate_game_file_list_json --settings_json .tempo.json

exit /b