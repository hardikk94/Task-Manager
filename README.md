# Task Manager & Expense Tracker

A comprehensive command-line application for managing tasks and tracking expenses with user authentication and persistent data storage.

## Features

### User Authentication
- **Registration**: Create a new account with username and password
- **Login**: Secure login with password hashing (SHA-256)
- **User Isolation**: Each user's data is stored separately and securely

### Task Manager
- ✅ **Add Tasks**: Create new tasks with descriptions
- 📋 **View Tasks**: Display all tasks with status and creation date
- ✓ **Mark as Completed**: Update task status from Pending to Completed
- 🗑️ **Delete Tasks**: Remove tasks from your list
- 📊 **Task Summary**: View count of total, pending, and completed tasks

### Expense Tracker
- 💰 **Add Expenses**: Record expenses with category, amount, and description
- 📊 **View Expenses**: Display all expenses with date, category, and amount
- 💵 **Budget Tracking**: Set monthly budget and track spending
- ⚠️ **Budget Alerts**: Get warnings when approaching or exceeding budget
- 📁 **Category Summary**: View total expenses grouped by category
- 💾 **CSV Export**: Expenses are automatically saved to CSV files
- 🗑️ **Delete Expenses**: Remove incorrect or unwanted expense entries

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd "Task Manager"
   ```

No additional packages are required as the application uses only Python standard library modules.

## Usage

### Starting the Application

Run the main application:
```bash
python main.py
```

### First Time Setup

1. **Register a New Account**
   - Choose option "2" from the authentication menu
   - Enter a unique username
   - Enter a password (minimum 4 characters)
   - Confirm your password

2. **Login**
   - Choose option "1" from the authentication menu
   - Enter your username and password

### Managing Tasks

From the main menu, select "1. Task Manager" to access:

- **Add a Task**: Enter a task description
- **View Tasks**: See all your tasks with their status
- **Mark as Completed**: Select a task by ID to mark it complete
- **Delete a Task**: Remove a task by its ID

### Managing Expenses

From the main menu, select "2. Expense Tracker" to access:

- **Add Expense**: Enter category, amount, and optional description
- **View Expenses**: See all recorded expenses
- **Track Budget**:
  - Set your monthly budget
  - View budget status and remaining balance
- **Save Expenses**: Manually save expenses (auto-saves after adding)
- **Delete Expense**: Remove an expense by its number
- **Category Summary**: View total expenses by category

## Data Storage

The application stores data in the following structure:

```
Task Manager/
├── data/
│   ├── users.json          # User credentials (hashed passwords)
│   ├── tasks.json          # All users' tasks
│   └── expenses/
│       ├── username_expenses.csv     # User's expenses
│       └── username_budget.txt       # User's budget
├── main.py                 # Main application
├── auth.py                 # Authentication module
├── task_manager.py         # Task management module
├── expense_tracker.py      # Expense tracking module
├── utils.py                # Utility functions
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Security Features

- **Password Hashing**: Passwords are hashed using SHA-256 before storage
- **User Isolation**: Each user can only access their own data
- **Input Validation**: All user inputs are validated to prevent errors
- **Secure Storage**: Credentials and data are stored in separate files

## Module Documentation

### auth.py
Handles user authentication with registration and login functionality. Passwords are securely hashed before storage.

### task_manager.py
Manages task operations including creation, viewing, updating status, and deletion. Each task has a unique ID, description, status, and timestamp.

### expense_tracker.py
Handles expense recording and budget tracking. Supports CSV export, category-based filtering, and budget monitoring with alerts.

### utils.py
Provides utility functions for UI operations including screen clearing, formatted printing, input validation, and user confirmations.

### main.py
The main application entry point that ties all modules together with an interactive menu system.

## Example Workflow

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Register and login**
   - Create a new account
   - Login with your credentials

3. **Manage tasks**
   - Add tasks like "Buy groceries", "Complete assignment"
   - Mark tasks as completed when done
   - View all tasks to track progress

4. **Track expenses**
   - Set a monthly budget (e.g., $1000)
   - Add expenses with categories (Food, Transport, etc.)
   - Check budget status to see remaining balance
   - View category summary to see spending patterns

5. **Logout when done**
   - Your data is automatically saved
   - Login again anytime to continue

## Tips for Best Use

1. **Task Management**
   - Use clear, descriptive task names
   - Regularly mark completed tasks to track progress
   - Delete old or irrelevant tasks to keep your list clean

2. **Expense Tracking**
   - Set a realistic monthly budget
   - Record expenses immediately to avoid forgetting
   - Use consistent category names for better summaries
   - Review category summary regularly to identify spending patterns

3. **Data Management**
   - Data is automatically saved after each operation
   - Back up the `data/` folder regularly
   - Keep your password secure and memorable

## Troubleshooting

### "File not found" errors
The application automatically creates necessary directories and files on first run.

### Cannot login
- Ensure you're using the correct username and password
- Username is case-insensitive
- Password is case-sensitive and must match exactly

### Data not saving
- Ensure you have write permissions in the project directory
- Check that the `data/` folder exists and is writable

## Requirements

- Python 3.6+
- Operating System: Windows, macOS, or Linux

## License

This project is created for educational purposes as part of the IITK curriculum.

## Support

For issues or questions, please review the code documentation or contact the development team.

---

**Version**: 1.0.0  
**Last Updated**: October 2025

