@echo off
echo Installing NextWatch...

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python...
    :: Download Python installer
    powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe', 'python_installer.exe')"
    :: Run the Python installer silently
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    :: Remove the installer after installation
    del python_installer.exe
) ELSE (
    echo Python is already installed.
)

:: Install required Python packages
echo Installing required Python packages...
pip install -r requirements.txt

:: Create nextwatch.bat for easy access in terminal
echo Creating NextWatch command...
echo @echo off > nextwatch.bat
echo python "%~dp0nextwatch.py" %%* >> nextwatch.bat
echo nextwatch.bat has been created. You can now run "NextWatch" from the terminal.

:: Add script directory to PATH (optional)
echo Adding script directory to PATH...
setx PATH "%PATH%;%cd%"

echo Installation complete. You can now use NextWatch from the terminal.
pause
