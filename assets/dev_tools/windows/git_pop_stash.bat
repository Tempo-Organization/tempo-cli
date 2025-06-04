@echo off
cd /d "%~dp0"
cd /d "..\..\.."

:show_stashes
cls
echo Current git stashes:
git stash list
echo.

set "stashes="
set /p stashes=Enter stash index(es) to pop (space separated), or press Enter to exit:

if "%stashes%"=="" goto end

for %%s in (%stashes%) do (
    echo Popping stash %%s...
    git stash pop stash@{%%s}
    timeout /t 2 /nobreak >nul
    cls
    echo After popping stash %%s, remaining stashes:
    git stash list
    echo.
)

goto show_stashes

:end
echo Exiting...
exit /b
