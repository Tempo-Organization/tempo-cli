@echo off
cd /d "%~dp0"
cd /d "..\..\.."

:start

set "pathToAdd="
set /p pathToAdd=Enter a path to add or drag a file over this window (press Enter to exit):

if "%pathToAdd%"=="" goto end

set "stashcomment="
set /p stashcomment=Enter a comment/message for this stash:

if "%stashcomment%"=="" (
    echo Stash comment cannot be empty. Please try again.
    goto start
)

git stash push "%pathToAdd%" -m "%stashcomment%"

echo.
echo Stash created for "%pathToAdd%" with comment: %stashcomment%
echo.

goto start

:end
echo Exiting...
exit /b
