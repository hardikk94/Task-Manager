"""
Task Manager and Expense Tracker Application
Main entry point for the application
"""

from auth import Authentication
from task_manager import TaskManager
from expense_tracker import ExpenseTracker
from utils import clear_screen, print_header, print_separator, get_input, confirm_action, pause


class Application:
    def __init__(self):
        """Initialize the application"""
        self.auth = Authentication()
        self.current_user = None
        self.task_manager = None
        self.expense_tracker = None
    
    def run(self):
        """Main application loop"""
        clear_screen()
        print_header("Welcome to Task Manager & Expense Tracker")
        
        while True:
            if not self.current_user:
                self.show_auth_menu()
            else:
                self.show_main_menu()
    
    def show_auth_menu(self):
        """Display authentication menu"""
        print("\n")
        print_separator()
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print_separator()
        
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            print("\nThank you for using Task Manager & Expense Tracker. Goodbye!")
            exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            pause()
    
    def register(self):
        """Handle user registration"""
        clear_screen()
        print_header("User Registration")
        
        print("\nPlease create your account:")
        username = get_input("Username: ")
        if not username:
            return
        
        password = get_input("Password (min 4 characters): ")
        if not password:
            return
        
        confirm_password = get_input("Confirm Password: ")
        if not confirm_password:
            return
        
        if password != confirm_password:
            print("\nPasswords do not match. Please try again.")
            pause()
            return
        
        success, message = self.auth.register(username, password)
        print(f"\n{message}")
        pause()
        
        if success:
            clear_screen()
    
    def login(self):
        """Handle user login"""
        clear_screen()
        print_header("User Login")
        
        username = get_input("\nUsername: ")
        if not username:
            return
        
        password = get_input("Password: ")
        if not password:
            return
        
        success, message = self.auth.login(username, password)
        print(f"\n{message}")
        
        if success:
            self.current_user = username.lower()
            self.task_manager = TaskManager(self.current_user)
            self.expense_tracker = ExpenseTracker(self.current_user)
            pause()
            clear_screen()
        else:
            pause()
    
    def logout(self):
        """Handle user logout"""
        if confirm_action("Are you sure you want to logout?"):
            self.current_user = None
            self.task_manager = None
            self.expense_tracker = None
            print("\nLogged out successfully!")
            pause()
            clear_screen()
    
    def show_main_menu(self):
        """Display main menu for logged-in users"""
        print_header(f"Main Menu - Welcome {self.current_user}!")
        print("\n1. Task Manager")
        print("2. Expense Tracker")
        print("3. Logout")
        print_separator()
        
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == "1":
            self.task_manager_menu()
        elif choice == "2":
            self.expense_tracker_menu()
        elif choice == "3":
            self.logout()
        else:
            print("\nInvalid choice. Please try again.")
            pause()
            clear_screen()
    
    def task_manager_menu(self):
        """Task manager submenu"""
        while True:
            clear_screen()
            print_header("Task Manager")
            
            # Show task summary
            counts = self.task_manager.get_task_count()
            print(f"\nTotal Tasks: {counts['total']} | Pending: {counts['pending']} | Completed: {counts['completed']}")
            
            print("\n1. Add a Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete a Task")
            print("5. Back to Main Menu")
            print_separator()
            
            choice = get_input("Enter your choice (1-5): ")
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.mark_task_completed()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                clear_screen()
                break
            else:
                print("\nInvalid choice. Please try again.")
                pause()
    
    def add_task(self):
        """Add a new task"""
        print("\n")
        print_separator()
        print("Add New Task")
        print_separator()
        
        description = get_input("Enter task description: ")
        if not description:
            return
        
        success, message = self.task_manager.add_task(description)
        print(f"\n{message}")
        pause()
    
    def view_tasks(self):
        """View all tasks"""
        clear_screen()
        print_header("Your Tasks")
        
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("\nNo tasks found. Start by adding a new task!")
        else:
            print(f"\n{'ID':<5} {'Status':<12} {'Description':<40} {'Created':<20}")
            print_separator()
            
            for task in tasks:
                task_id = task['id']
                status = task['status']
                description = task['description'][:40]
                created = task.get('created_at', 'N/A')[:19]
                
                print(f"{task_id:<5} {status:<12} {description:<40} {created:<20}")
        
        pause()
    
    def mark_task_completed(self):
        """Mark a task as completed"""
        print("\n")
        print_separator()
        print("Mark Task as Completed")
        print_separator()
        
        # Show pending tasks
        tasks = [t for t in self.task_manager.get_all_tasks() if t['status'] == 'Pending']
        
        if not tasks:
            print("\nNo pending tasks to mark as completed!")
            pause()
            return
        
        print(f"\n{'ID':<5} {'Description':<50}")
        print_separator()
        for task in tasks:
            print(f"{task['id']:<5} {task['description']:<50}")
        
        print()
        task_id = get_input("Enter task ID to mark as completed: ")
        if not task_id:
            return
        
        success, message = self.task_manager.mark_completed(task_id)
        print(f"\n{message}")
        pause()
    
    def delete_task(self):
        """Delete a task"""
        print("\n")
        print_separator()
        print("Delete Task")
        print_separator()
        
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("\nNo tasks to delete!")
            pause()
            return
        
        print(f"\n{'ID':<5} {'Status':<12} {'Description':<50}")
        print_separator()
        for task in tasks:
            print(f"{task['id']:<5} {task['status']:<12} {task['description']:<50}")
        
        print()
        task_id = get_input("Enter task ID to delete: ")
        if not task_id:
            return
        
        if confirm_action("Are you sure you want to delete this task?"):
            success, message = self.task_manager.delete_task(task_id)
            print(f"\n{message}")
            pause()
    
    def expense_tracker_menu(self):
        """Expense tracker submenu"""
        while True:
            clear_screen()
            print_header("Expense Tracker")
            
            # Show budget summary
            total = self.expense_tracker.get_total_expenses()
            budget = self.expense_tracker.monthly_budget
            print(f"\nTotal Expenses: ${total:.2f} | Monthly Budget: ${budget:.2f}")
            
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. Track Budget")
            print("4. Save Expenses")
            print("5. Delete Expense")
            print("6. Category Summary")
            print("7. Back to Main Menu")
            print_separator()
            
            choice = get_input("Enter your choice (1-7): ")
            
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.track_budget()
            elif choice == "4":
                self.save_expenses()
            elif choice == "5":
                self.delete_expense()
            elif choice == "6":
                self.view_category_summary()
            elif choice == "7":
                clear_screen()
                break
            else:
                print("\nInvalid choice. Please try again.")
                pause()
    
    def add_expense(self):
        """Add a new expense"""
        print("\n")
        print_separator()
        print("Add New Expense")
        print_separator()
        
        category = get_input("Enter expense category (e.g., Food, Transport, Entertainment): ")
        if not category:
            return
        
        amount = get_input("Enter amount: $", float)
        if amount is None:
            return
        
        description = get_input("Enter description (optional): ", allow_empty=True)
        if description is None:
            description = ""
        
        success, message = self.expense_tracker.add_expense(category, amount, description)
        print(f"\n{message}")
        
        # Auto-save after adding
        self.expense_tracker._save_expenses()
        pause()
    
    def view_expenses(self):
        """View all expenses"""
        clear_screen()
        print_header("Your Expenses")
        
        expenses = self.expense_tracker.get_all_expenses()
        
        if not expenses:
            print("\nNo expenses found. Start by adding a new expense!")
        else:
            print(f"\n{'#':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
            print_separator()
            
            for idx, expense in enumerate(expenses):
                num = idx + 1
                date = expense['date']
                category = expense['category'][:15]
                amount = f"${expense['amount']:.2f}"
                description = expense['description'][:30]
                
                print(f"{num:<4} {date:<12} {category:<15} {amount:<10} {description:<30}")
            
            print_separator()
            total = self.expense_tracker.get_total_expenses()
            print(f"{'Total:':<31} ${total:.2f}")
        
        pause()
    
    def track_budget(self):
        """Track budget and show status"""
        clear_screen()
        print_header("Budget Tracking")
        
        print("\n1. Set Monthly Budget")
        print("2. View Budget Status")
        print("3. Back")
        print_separator()
        
        choice = get_input("Enter your choice (1-3): ")
        
        if choice == "1":
            print()
            amount = get_input("Enter your monthly budget: $", float)
            if amount is not None:
                success, message = self.expense_tracker.set_budget(amount)
                print(f"\n{message}")
                pause()
        
        elif choice == "2":
            status = self.expense_tracker.get_budget_status()
            
            print("\n")
            print_separator()
            print(f"Monthly Budget:     ${status['budget']:.2f}")
            print(f"Total Spent:        ${status['spent']:.2f}")
            print(f"Remaining:          ${status['remaining']:.2f}")
            print(f"Percentage Used:    {status['percentage_used']:.1f}%")
            print_separator()
            
            if status['over_budget']:
                print(f"\n⚠️  WARNING: You have exceeded your budget by ${abs(status['remaining']):.2f}!")
            elif status['remaining'] < status['budget'] * 0.2:
                print(f"\n⚠️  CAUTION: You have ${status['remaining']:.2f} left (less than 20% of budget)")
            else:
                print(f"\n✓ You are within your budget. Keep it up!")
            
            pause()
    
    def save_expenses(self):
        """Save expenses to file"""
        print("\n")
        self.expense_tracker._save_expenses()
        print("All expenses saved successfully!")
        pause()
    
    def delete_expense(self):
        """Delete an expense"""
        expenses = self.expense_tracker.get_all_expenses()
        
        if not expenses:
            print("\nNo expenses to delete!")
            pause()
            return
        
        print("\n")
        print_separator()
        print("Delete Expense")
        print_separator()
        
        print(f"\n{'#':<4} {'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
        print_separator()
        
        for idx, expense in enumerate(expenses):
            num = idx + 1
            date = expense['date']
            category = expense['category'][:15]
            amount = f"${expense['amount']:.2f}"
            description = expense['description'][:30]
            
            print(f"{num:<4} {date:<12} {category:<15} {amount:<10} {description:<30}")
        
        print()
        index = get_input("Enter expense number to delete: ", int)
        if index is None:
            return
        
        if confirm_action("Are you sure you want to delete this expense?"):
            success, message = self.expense_tracker.delete_expense(index - 1)
            print(f"\n{message}")
            pause()
    
    def view_category_summary(self):
        """View expenses grouped by category"""
        clear_screen()
        print_header("Expenses by Category")
        
        summary = self.expense_tracker.get_category_summary()
        
        if not summary:
            print("\nNo expenses found!")
        else:
            print(f"\n{'Category':<20} {'Total Amount':<15}")
            print_separator()
            
            for category, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
                print(f"{category:<20} ${amount:.2f}")
            
            print_separator()
            total = sum(summary.values())
            print(f"{'Grand Total:':<20} ${total:.2f}")
        
        pause()


def main():
    """Main entry point"""
    try:
        app = Application()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Goodbye!")
        exit(0)
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
        print("Please contact support if the problem persists.")
        exit(1)


if __name__ == "__main__":
    main()

