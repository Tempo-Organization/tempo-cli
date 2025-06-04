@echo off

cd /d "%~dp0"

cd /d "..\..\.."

git switch dev

exit /b
