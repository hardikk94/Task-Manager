# Quick Start Guide

## Running the Application

### Option 1: Using the Quick Start Script (Recommended)

**On macOS/Linux:**
```bash
./run.sh
```

**On Windows:**
```bash
run.bat
```

### Option 2: Direct Python Command

**On macOS/Linux:**
```bash
python3 main.py
```

**On Windows:**
```bash
python main.py
```

## First Time User Guide

### Step 1: Register an Account

1. Run the application
2. From the authentication menu, select **2** (Register)
3. Enter a unique username (e.g., "john_doe")
4. Enter a password (minimum 4 characters)
5. Confirm your password
6. You'll see "Registration successful!"

### Step 2: Login

1. From the authentication menu, select **1** (Login)
2. Enter your username
3. Enter your password
4. You'll see "Welcome back, [username]!"

### Step 3: Try Task Manager

1. From the main menu, select **1** (Task Manager)
2. Select **1** to add a task
3. Enter a task description (e.g., "Complete Python assignment")
4. Select **2** to view your tasks
5. Try marking a task as completed by selecting **3**

### Step 4: Try Expense Tracker

1. From the main menu, select **2** (Expense Tracker)
2. Select **3** to track budget, then **1** to set a budget (e.g., 1000)
3. Select **1** to add an expense
   - Category: "Food"
   - Amount: 50
   - Description: "Lunch at cafe"
4. Select **2** to view all expenses
5. Select **3** then **2** to check your budget status

## Common Tasks

### Managing Tasks

- **Add Task**: Task Manager → 1
- **View Tasks**: Task Manager → 2
- **Complete Task**: Task Manager → 3
- **Delete Task**: Task Manager → 4

### Managing Expenses

- **Add Expense**: Expense Tracker → 1
- **View Expenses**: Expense Tracker → 2
- **Set Budget**: Expense Tracker → 3 → 1
- **Check Budget**: Expense Tracker → 3 → 2
- **Category Summary**: Expense Tracker → 6

## Tips

1. **Data Persistence**: All your data is automatically saved to the `data/` folder
2. **Multiple Users**: Each user has their own separate data
3. **Security**: Passwords are securely hashed (not stored in plain text)
4. **Budget Alerts**: You'll get warnings when you exceed 80% of your budget
5. **CSV Export**: Expenses are saved in CSV format for easy import to Excel

## Example Session

```
1. Register with username "alice" and password "secure123"
2. Login with the same credentials
3. Add tasks:
   - "Buy groceries"
   - "Finish project report"
   - "Call dentist"
4. Set monthly budget to $2000
5. Add expenses:
   - Food: $45.50 (Dinner with friends)
   - Transport: $30.00 (Taxi to work)
   - Entertainment: $15.00 (Movie ticket)
6. View budget status
7. Mark "Call dentist" as completed
8. Logout
```

## Troubleshooting

### "command not found: python"
- On macOS/Linux, use `python3` instead of `python`
- Make sure Python 3.6+ is installed

### "Permission denied" when running run.sh
```bash
chmod +x run.sh
```

### Data not saving
- Ensure you have write permissions in the project directory
- The application will create a `data/` folder automatically

## Project Structure

```
Task Manager/
├── main.py              # Start here!
├── auth.py              # User authentication
├── task_manager.py      # Task operations
├── expense_tracker.py   # Expense operations
├── utils.py             # Helper functions
├── run.sh               # Quick start (Unix)
├── run.bat              # Quick start (Windows)
├── README.md            # Full documentation
├── QUICKSTART.md        # This file
└── data/                # Your data (auto-created)
```

## Need Help?

- Read the full `README.md` for detailed documentation
- Check that Python 3.6+ is installed: `python3 --version`
- Make sure you're in the project directory when running the app

## Sample User Flow

```
Welcome to Task Manager & Expense Tracker
============================================================

--------------------------------------------------
1. Login
2. Register
3. Exit
--------------------------------------------------
Enter your choice (1-3): 2

============================================================
                     User Registration
============================================================

Please create your account:
Username: testuser
Password (min 4 characters): test1234
Confirm Password: test1234

Registration successful! You can now log in.

[Login with testuser...]

============================================================
          Main Menu - Welcome testuser!
============================================================

1. Task Manager
2. Expense Tracker
3. Logout
--------------------------------------------------
```

Happy organizing! 🎯💰

