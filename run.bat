@echo off

echo ================================
echo Starting MILS AI Assistant
echo ================================

cd /d %~dp0

echo Checking virtual environment...

IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Web Server...

start http://127.0.0.1:5000

python web_app.py

pause