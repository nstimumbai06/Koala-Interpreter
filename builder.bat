@echo off
setlocal enabledelayedexpansion
set ERRORLEVEL=0

echo Building standalone executable using PyInstaller...
pyinstaller --onefile --name koala koala_interpreter.py
if %ERRORLEVEL% neq 0 (
    echo PyInstaller build failed!
    exit /b 1
)

if not exist "dist\koala.exe" (
    echo Build failed: koala.exe not found in dist folder!
    exit /b 1
)

echo Packaging executable using Inno Setup Compiler...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer_script.iss
if %ERRORLEVEL% neq 0 (
    echo Inno Setup Compiler packaging failed!
    exit /b 1
)

echo Build and packaging completed successfully!
start "" "Output\KoalaInstaller.exe"
pause
