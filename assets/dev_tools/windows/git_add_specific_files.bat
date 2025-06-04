@echo off
cd /d "%~dp0"

cd /d "..\..\.."

:loop


set /p pathToAdd=Enter a path to add or drag a file over this window (press Enter to finish):
if "%pathToAdd%"=="" goto end

git add "%pathToAdd%"
echo Added "%pathToAdd%"

goto loop

:end
echo Done adding paths.
pause
