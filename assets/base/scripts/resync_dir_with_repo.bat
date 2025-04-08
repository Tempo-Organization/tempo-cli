@echo off


cd "%~dp0"

cd ..

taskkill /f /im "tempo.exe" > nul 2>&1

set exe_file="%CD%\tempo.exe"
set settings_json="%CD%\presets\default\settings.json"
set arg=resync_dir_with_repo

%exe_file% %arg% --settings_json %settings_json%

exit /b
