@echo off

echo ============================================
echo         MILS AI Assistant (Web Mode)
echo ============================================

REM ===== Check Python =====
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit
)

REM ===== Create Virtual Environment =====
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM ===== Activate venv =====
call venv\Scripts\activate

REM ===== Upgrade pip =====
echo Upgrading pip...
python -m pip install --upgrade pip

REM ===== Install dependencies =====
echo Installing requirements...
pip install -r requirements.txt

REM ===== Start Ollama =====
echo Checking Ollama server...

tasklist | find /i "ollama.exe" >nul
if errorlevel 1 (
    echo Starting Ollama server...
    start "" ollama serve
    timeout /t 5 >nul
) else (
    echo Ollama already running
)

REM ===== Pull Phi model =====
echo Downloading AI model if not present...
ollama pull phi

REM ===== Start Web App =====
echo Starting Web Application...

start http://localhost:5000

python web_app.py

pause