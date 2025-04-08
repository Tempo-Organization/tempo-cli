@echo off

cd /d "%~dp0"

cd ..

taskkill /f /im "tempo.exe" > nul 2>&1

set exe_file="%CD%\tempo.exe"
set settings_json="%CD%\presets\default\settings.json"
set arg=build

%exe_file% %arg% --settings_json %settings_json%

exit /b
