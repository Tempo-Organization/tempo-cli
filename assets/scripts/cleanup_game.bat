@echo off

cd /d "%~dp0"

cd ../..

uv run tempo_cli cleanup_game --settings_json .tempo.json --output_json "%CD%/Modding/game_file_list.json"

exit /b