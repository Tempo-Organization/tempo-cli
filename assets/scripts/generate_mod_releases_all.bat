@echo off

cd /d "%~dp0"

cd ../..

set "release_packaging_dir=%CD%\Modding\mod_packaging\releases"

mkdir %release_packaging_dir%

set "output_dir=%CD%\Modding\mod_packaging\output"

mkdir %output_dir%

uv run tempo_cli generate_mod_releases_all --settings_json .tempo.json --base_files_directory %release_packaging_dir% --output_directory %output_dir%

exit /b