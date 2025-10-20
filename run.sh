#!/bin/bash
# Quick start script for Task Manager & Expense Tracker

echo "Starting Task Manager & Expense Tracker..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

# Run the application
python3 main.py

