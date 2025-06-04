@echo off
setlocal

:: Check if 'hatch' command exists
hatch --version >nul 2>&1
if %errorlevel%==0 (
    rem echo Hatch is already installed.
    exit /b 0
)

:: Hatch not found, install it using pip
echo Hatch not found. Installing via pip...
python -m pip install hatch

:: Re-check installation
hatch --version >nul 2>&1
if %errorlevel%==0 (
    echo Hatch installed successfully.
) else (
    echo Failed to install Hatch. Make sure Python and pip are properly configured in PATH.
    exit /b 1
)

endlocal
