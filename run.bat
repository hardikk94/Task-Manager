@echo off
REM Quick start script for Task Manager & Expense Tracker (Windows)

echo Starting Task Manager & Expense Tracker...
echo.

REM Check if Python is available
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

REM Run the application
python main.py
pause

