"""
Expense Tracker Module
Handles expense management and budget tracking
"""

import csv
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class ExpenseTracker:
    def __init__(self, username: str, expenses_dir="data/expenses"):
        """Initialize expense tracker for a specific user"""
        self.username = username.lower()
        self.expenses_dir = expenses_dir
        self.expenses_file = os.path.join(expenses_dir, f"{self.username}_expenses.csv")
        self.budget_file = os.path.join(expenses_dir, f"{self.username}_budget.txt")
        self._ensure_data_directory()
        self.expenses = []
        self.monthly_budget = 0.0
        self._load_expenses()
        self._load_budget()
    
    def _ensure_data_directory(self):
        """Create expenses directory if it doesn't exist"""
        if not os.path.exists(self.expenses_dir):
            os.makedirs(self.expenses_dir)
    
    def _load_expenses(self):
        """Load expenses from CSV file"""
        if os.path.exists(self.expenses_file):
            try:
                with open(self.expenses_file, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    self.expenses = list(reader)
                    # Convert amount to float
                    for expense in self.expenses:
                        expense['amount'] = float(expense['amount'])
            except (csv.Error, ValueError):
                self.expenses = []
        else:
            self.expenses = []
    
    def _save_expenses(self):
        """Save expenses to CSV file"""
        if not self.expenses:
            # If no expenses, create an empty file with headers
            with open(self.expenses_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
                writer.writeheader()
            return
        
        with open(self.expenses_file, 'w', newline='') as f:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)
    
    def _load_budget(self):
        """Load monthly budget from file"""
        if os.path.exists(self.budget_file):
            try:
                with open(self.budget_file, 'r') as f:
                    self.monthly_budget = float(f.read().strip())
            except ValueError:
                self.monthly_budget = 0.0
        else:
            self.monthly_budget = 0.0
    
    def _save_budget(self):
        """Save monthly budget to file"""
        with open(self.budget_file, 'w') as f:
            f.write(str(self.monthly_budget))
    
    def add_expense(self, category: str, amount: float, description: str = "") -> Tuple[bool, str]:
        """
        Add a new expense
        Returns: (success: bool, message: str)
        """
        # Validate category
        if not category or len(category.strip()) == 0:
            return False, "Category cannot be empty"
        
        # Validate amount
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Amount must be greater than 0"
        except ValueError:
            return False, "Invalid amount. Please enter a valid number"
        
        expense = {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'category': category.strip(),
            'amount': amount,
            'description': description.strip()
        }
        
        self.expenses.append(expense)
        self._save_expenses()
        
        return True, f"Expense of ${amount:.2f} added successfully!"
    
    def get_all_expenses(self) -> List[Dict]:
        """Get all expenses"""
        return self.expenses
    
    def get_expenses_by_category(self, category: str) -> List[Dict]:
        """Get expenses filtered by category"""
        return [exp for exp in self.expenses if exp['category'].lower() == category.lower()]
    
    def get_total_expenses(self) -> float:
        """Calculate total expenses"""
        return sum(exp['amount'] for exp in self.expenses)
    
    def set_budget(self, amount: float) -> Tuple[bool, str]:
        """
        Set monthly budget
        Returns: (success: bool, message: str)
        """
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Budget must be greater than 0"
        except ValueError:
            return False, "Invalid amount. Please enter a valid number"
        
        self.monthly_budget = amount
        self._save_budget()
        
        return True, f"Monthly budget set to ${amount:.2f}"
    
    def get_budget_status(self) -> Dict:
        """
        Get budget status and remaining balance
        Returns: dict with budget info
        """
        total_expenses = self.get_total_expenses()
        remaining = self.monthly_budget - total_expenses
        
        status = {
            'budget': self.monthly_budget,
            'spent': total_expenses,
            'remaining': remaining,
            'over_budget': remaining < 0,
            'percentage_used': (total_expenses / self.monthly_budget * 100) if self.monthly_budget > 0 else 0
        }
        
        return status
    
    def delete_expense(self, index: int) -> Tuple[bool, str]:
        """
        Delete an expense by index
        Returns: (success: bool, message: str)
        """
        if index < 0 or index >= len(self.expenses):
            return False, "Invalid expense index"
        
        deleted_expense = self.expenses.pop(index)
        self._save_expenses()
        
        return True, f"Expense '{deleted_expense['description']}' of ${deleted_expense['amount']:.2f} deleted successfully!"
    
    def get_category_summary(self) -> Dict[str, float]:
        """Get total expenses grouped by category"""
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category in summary:
                summary[category] += expense['amount']
            else:
                summary[category] = expense['amount']
        
        return summary

