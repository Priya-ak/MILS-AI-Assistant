@echo off

echo Starting MILS AI Assistant...

call venv\Scripts\activate

echo Starting AI Camera System...
start cmd /k python main.py

echo Starting Web Server...
start cmd /k python web_app.py

timeout /t 5

echo Opening Dashboard...
start http://127.0.0.1:5000

pause