@echo off
pip3 install pyinstaller
pyinstaller main.pyw -i "NONE" --onefile
cd dist
copy main.exe ..
cd ..
del main.spec
rd /q /s build dist
set /p DUMMY=Press any key to exit...