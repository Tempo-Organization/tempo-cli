@echo off

cd /d "%~dp0"

cd ../..

uv run cz commit

exit /b