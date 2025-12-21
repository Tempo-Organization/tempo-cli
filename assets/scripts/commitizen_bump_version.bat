@echo off

cd /d "%~dp0"

cd ../..

uv run cz bump

exit /b