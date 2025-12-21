@echo off

cd /d "%~dp0"

cd ../..

uv lock --upgrade

uv sync

exit /b