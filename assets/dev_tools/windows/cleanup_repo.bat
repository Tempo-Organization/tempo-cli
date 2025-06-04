@echo of

cd /d "%~dp0"

call install_hatch.bat

cd /d "..\..\.."

hatch run scripts:clean

exit /b
