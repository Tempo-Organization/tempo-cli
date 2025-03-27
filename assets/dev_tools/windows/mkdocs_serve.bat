@echo off

cd /d "%~dp0"

cd ../../..

mkdocs serve

exit /b