@echo off

echo Setting up MILS AI Assistant...

python -m venv venv
call venv\Scripts\activate

pip install -r requirements.txt

echo Setup completed!
pause