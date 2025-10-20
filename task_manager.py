"""
Task Manager Module
Handles task creation, viewing, updating, and deletion
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class TaskManager:
    def __init__(self, username: str, tasks_file="data/tasks.json"):
        """Initialize task manager for a specific user"""
        self.username = username.lower()
        self.tasks_file = tasks_file
        self._ensure_data_directory()
        self._load_tasks()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        data_dir = os.path.dirname(self.tasks_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_tasks(self):
        """Load all tasks from file"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r') as f:
                    all_tasks = json.load(f)
            except json.JSONDecodeError:
                all_tasks = {}
        else:
            all_tasks = {}
        
        # Get tasks for current user
        self.tasks = all_tasks.get(self.username, {})
        self.all_tasks = all_tasks
    
    def _save_tasks(self):
        """Save tasks to file"""
        self.all_tasks[self.username] = self.tasks
        with open(self.tasks_file, 'w') as f:
            json.dump(self.all_tasks, f, indent=4)
    
    def _generate_task_id(self) -> str:
        """Generate a unique task ID"""
        if not self.tasks:
            return "1"
        
        # Get the maximum task ID and increment
        max_id = max([int(task_id) for task_id in self.tasks.keys()])
        return str(max_id + 1)
    
    def add_task(self, description: str) -> Tuple[bool, str]:
        """
        Add a new task
        Returns: (success: bool, message: str)
        """
        if not description or len(description.strip()) == 0:
            return False, "Task description cannot be empty"
        
        task_id = self._generate_task_id()
        
        self.tasks[task_id] = {
            "id": task_id,
            "description": description.strip(),
            "status": "Pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self._save_tasks()
        return True, f"Task added successfully! Task ID: {task_id}"
    
    def get_all_tasks(self) -> List[Dict]:
        """Get all tasks for the current user"""
        return list(self.tasks.values())
    
    def get_task(self, task_id: str) -> Optional[Dict]:
        """Get a specific task by ID"""
        return self.tasks.get(task_id)
    
    def mark_completed(self, task_id: str) -> Tuple[bool, str]:
        """
        Mark a task as completed
        Returns: (success: bool, message: str)
        """
        if task_id not in self.tasks:
            return False, f"Task ID {task_id} not found"
        
        if self.tasks[task_id]["status"] == "Completed":
            return False, "Task is already marked as completed"
        
        self.tasks[task_id]["status"] = "Completed"
        self.tasks[task_id]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self._save_tasks()
        return True, f"Task {task_id} marked as completed!"
    
    def delete_task(self, task_id: str) -> Tuple[bool, str]:
        """
        Delete a task
        Returns: (success: bool, message: str)
        """
        if task_id not in self.tasks:
            return False, f"Task ID {task_id} not found"
        
        task_desc = self.tasks[task_id]["description"]
        del self.tasks[task_id]
        
        self._save_tasks()
        return True, f"Task '{task_desc}' deleted successfully!"
    
    def get_task_count(self) -> Dict[str, int]:
        """Get count of tasks by status"""
        pending = sum(1 for task in self.tasks.values() if task["status"] == "Pending")
        completed = sum(1 for task in self.tasks.values() if task["status"] == "Completed")
        
        return {
            "total": len(self.tasks),
            "pending": pending,
            "completed": completed
        }

