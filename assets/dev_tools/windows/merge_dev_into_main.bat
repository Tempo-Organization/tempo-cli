@echo off
cd /d "%~dp0"

cd /d "..\..\.."

git checkout main

git pull origin main

git merge dev

git push origin main

exit /b
