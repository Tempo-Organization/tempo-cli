@echo off
cd /d "%~dp0"

call install_hatch.bat

cd /d "..\..\.."

hatch env create dev

hatch run pre-commit install

hatch run pre-commit install --hook-type commit-msg

exit /b
