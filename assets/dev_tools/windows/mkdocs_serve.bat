@echo off
cd /d "%~dp0"

call install_hatch.bat

cd /d "..\..\.."

hatch run mkdocs serve

exit /b
