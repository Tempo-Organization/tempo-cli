@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli generate_game_file_list_json --settings_json .tempo.json --output_json "%CD%/Modding/game_file_list.json"

exit /b