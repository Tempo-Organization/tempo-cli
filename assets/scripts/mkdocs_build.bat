@echo off

cd /d "%~dp0"

cd ../..

set "site_dir=%CD%\Modding\docs\site"
set "zip_path=%CD%\Modding\docs\docs.zip"

uv run mkdocs build --site-dir "%site_dir%"

uv run tempo_cli zip --directory %site_dir% --zip %zip_path%

exit /b
