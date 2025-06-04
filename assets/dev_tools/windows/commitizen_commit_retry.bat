@echo off
cd /d "%~dp0"

call install_hatch.bat

cd /d "..\..\.."

hatch run cz commit --all -- -s --retry

exit /b
