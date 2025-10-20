# Task Manager & Expense Tracker - Project Overview

## 🎯 Project Summary

A comprehensive Python-based command-line application that combines task management and expense tracking capabilities with secure user authentication. Built using only Python standard library modules, this application demonstrates file handling, data persistence, user authentication, and interactive menu-driven interfaces.

## 📋 Features Implemented

### ✅ User Authentication System
- User registration with unique username validation
- Secure password hashing using SHA-256
- Login authentication with credential verification
- Session management for logged-in users
- Persistent storage of user credentials

### ✅ Task Manager
- **Create Tasks**: Add tasks with unique IDs and descriptions
- **View Tasks**: Display all tasks with status, ID, and creation date
- **Update Tasks**: Mark tasks as completed
- **Delete Tasks**: Remove tasks from the list
- **Task Summary**: Real-time count of total, pending, and completed tasks
- **User Isolation**: Each user's tasks are stored separately

### ✅ Expense Tracker
- **Add Expenses**: Record expenses with date, category, amount, and description
- **View Expenses**: Display all expenses in a formatted table
- **Budget Management**: Set and track monthly budget
- **Budget Alerts**: Automatic warnings when exceeding budget thresholds
- **Category Summary**: Group and total expenses by category
- **CSV Export**: Automatic saving to CSV format for Excel compatibility
- **Delete Expenses**: Remove incorrect expense entries
- **Spending Analysis**: Track budget usage percentage

### ✅ Data Persistence
- JSON storage for users and tasks
- CSV storage for expenses
- Automatic file and directory creation
- Persistent budget tracking
- Data isolation per user

### ✅ User Interface
- Clear, intuitive menu-driven interface
- Cross-platform screen clearing
- Formatted tables and headers
- Input validation and error handling
- Confirmation prompts for destructive actions
- Real-time status updates

## 📁 Project Structure

```
Task Manager/
│
├── 📄 main.py                 # Main application entry point
│   └── Application class with menu system and user workflows
│
├── 🔐 auth.py                 # Authentication module
│   └── User registration, login, password hashing
│
├── ✅ task_manager.py         # Task management module
│   └── CRUD operations for tasks, task status tracking
│
├── 💰 expense_tracker.py     # Expense tracking module
│   └── Expense management, budget tracking, CSV handling
│
├── 🛠️ utils.py                # Utility functions
│   └── UI helpers, input validation, screen management
│
├── 📚 README.md              # Complete documentation
├── 🚀 QUICKSTART.md          # Quick start guide
├── 📋 requirements.txt       # Dependencies (standard library only)
├── 🎯 PROJECT_OVERVIEW.md    # This file
│
├── ▶️ run.sh                  # Quick start script (Unix/Linux/macOS)
├── ▶️ run.bat                 # Quick start script (Windows)
│
├── 🙈 .gitignore             # Git ignore rules
│
└── 📂 data/                  # Auto-created data directory
    ├── users.json            # User credentials (hashed)
    ├── tasks.json            # All users' tasks
    └── expenses/             # Expense data per user
        ├── {username}_expenses.csv
        └── {username}_budget.txt
```

## 🔧 Technical Implementation

### Modules Used (Standard Library Only)
- `hashlib` - SHA-256 password hashing
- `json` - User and task data storage
- `csv` - Expense data storage and export
- `os` - File and directory operations
- `datetime` - Timestamps and date tracking
- `typing` - Type hints for code clarity
- `platform` - Cross-platform compatibility

### Design Patterns
- **Object-Oriented Design**: Each module is a class with encapsulated functionality
- **Separation of Concerns**: Authentication, tasks, and expenses are separate modules
- **Single Responsibility**: Each function has one clear purpose
- **Data Persistence**: Automatic saving after each operation
- **Error Handling**: Comprehensive try-catch blocks and validation

### Security Features
- Password hashing (SHA-256)
- No plain-text password storage
- User data isolation
- Input validation and sanitization
- Case-insensitive username handling

## 📊 Data Models

### User Model
```python
{
    "username": {
        "password": "hashed_password_string"
    }
}
```

### Task Model
```python
{
    "username": {
        "task_id": {
            "id": "1",
            "description": "Task description",
            "status": "Pending" | "Completed",
            "created_at": "2025-10-20 10:30:00",
            "completed_at": "2025-10-20 15:45:00"  # Optional
        }
    }
}
```

### Expense Model (CSV)
```csv
date,category,amount,description
2025-10-20,Food,45.50,Lunch at cafe
2025-10-20,Transport,30.00,Taxi to work
```

## 🎯 Key Features Demonstration

### 1. User Authentication Flow
```
Register → Login → Access System → Logout
```

### 2. Task Management Flow
```
Add Task → View Tasks → Mark as Completed → Delete Task
```

### 3. Expense Tracking Flow
```
Set Budget → Add Expenses → View Expenses → Check Budget Status
```

### 4. Budget Monitoring
- ✅ Within budget (< 80%): Normal status
- ⚠️ Warning (80-100%): Caution message
- 🚨 Over budget (> 100%): Alert message with overage amount

## 💡 Usage Examples

### Example 1: Daily Task Management
```
1. Login to system
2. Add tasks: "Buy groceries", "Complete assignment", "Call dentist"
3. Complete "Call dentist"
4. View remaining tasks
5. Logout
```

### Example 2: Monthly Budget Tracking
```
1. Login to system
2. Set monthly budget: $1000
3. Record expenses throughout month
4. Check budget status regularly
5. View category summary to analyze spending
6. Export to CSV for detailed analysis
```

## 📈 Features Beyond Requirements

### Enhanced Task Features
- Task creation timestamp
- Task completion timestamp
- Real-time task count summary
- Formatted task display with alignment

### Enhanced Expense Features
- Category-wise expense summary
- Budget usage percentage
- Multi-level budget warnings
- Expense deletion capability
- CSV format for Excel compatibility
- Automatic data saving

### Enhanced User Experience
- Cross-platform compatibility
- Clear screen for better readability
- Formatted tables and separators
- Input validation with helpful messages
- Confirmation prompts for destructive actions
- Graceful error handling

## 🚀 How to Run

### Quick Start
```bash
# On macOS/Linux
./run.sh

# On Windows
run.bat

# Or directly with Python
python3 main.py
```

### First-Time Setup
1. Run the application
2. Register a new account
3. Login with your credentials
4. Explore Task Manager and Expense Tracker

## 📝 Code Quality

- ✅ Comprehensive docstrings for all modules and functions
- ✅ Type hints for function parameters and returns
- ✅ Clear variable and function names
- ✅ Consistent code formatting
- ✅ Error handling and validation
- ✅ No external dependencies
- ✅ Zero linter errors
- ✅ Cross-platform compatibility

## 🎓 Learning Outcomes

This project demonstrates:
1. File handling and data persistence
2. User authentication and security
3. Object-oriented programming
4. Menu-driven interface design
5. Input validation and error handling
6. CSV and JSON data formats
7. Cross-platform development
8. Code organization and modularity
9. Type hints and documentation
10. User experience design

## 📦 Deliverables

- ✅ Complete source code (5 Python modules)
- ✅ Comprehensive README.md
- ✅ Quick start guide
- ✅ Project overview (this file)
- ✅ Platform-specific run scripts
- ✅ Requirements documentation
- ✅ Git ignore configuration
- ✅ Zero external dependencies

## 🔍 Testing Recommendations

1. **Authentication Testing**
   - Register multiple users
   - Verify password hashing
   - Test login validation
   - Verify user data isolation

2. **Task Management Testing**
   - Add various tasks
   - Mark tasks as completed
   - Delete tasks
   - Verify task persistence

3. **Expense Tracking Testing**
   - Add expenses in different categories
   - Set and modify budget
   - Test budget alerts
   - Verify CSV export
   - Test category summary

4. **Error Handling Testing**
   - Try invalid inputs
   - Test empty inputs
   - Test boundary conditions
   - Verify error messages

## 🎉 Project Status

**Status**: ✅ COMPLETED

All requirements from the problem statement have been implemented:
- ✅ User authentication (registration & login)
- ✅ Password hashing for security
- ✅ Task management (add, view, mark completed, delete)
- ✅ Expense tracking (add, view, delete)
- ✅ Budget setting and tracking
- ✅ File handling for persistence (JSON & CSV)
- ✅ Interactive menu-driven interface
- ✅ User data isolation
- ✅ Comprehensive documentation

## 🌟 Bonus Features Included

- Task creation and completion timestamps
- Real-time task summary
- Category-wise expense analysis
- Budget usage percentage
- Multi-level budget warnings
- Expense deletion capability
- Cross-platform scripts
- Comprehensive error handling
- Beautiful formatted output
- User-friendly confirmations

---

**Version**: 1.0.0  
**Created**: October 2025  
**Python Version**: 3.6+  
**Dependencies**: None (Standard Library Only)

Ready to use! 🚀

