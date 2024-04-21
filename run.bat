@echo off

set VENV_PATH=venv

REM Check if venv exists
IF EXIST %VENV_PATH% (
    echo Virtual environment exists. Running app.py...
    call %VENV_PATH%\Scripts\activate.bat
    python app.py
) ELSE (
    echo Virtual environment does not exist. Creating venv and installing requirements...
    python -m venv %VENV_PATH%
    call %VENV_PATH%\Scripts\activate.bat
    pip install -r requirements.txt
    python app.py
)

pause