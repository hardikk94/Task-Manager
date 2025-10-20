"""
User Authentication Module
Handles user registration, login, and credential management
"""

import hashlib
import json
import os
from typing import Optional, Tuple


class Authentication:
    def __init__(self, users_file="data/users.json"):
        """Initialize authentication system"""
        self.users_file = users_file
        self._ensure_data_directory()
        self._load_users()
    
    def _ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        data_dir = os.path.dirname(self.users_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_users(self):
        """Load users from file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    self.users = json.load(f)
            except json.JSONDecodeError:
                self.users = {}
        else:
            self.users = {}
    
    def _save_users(self):
        """Save users to file"""
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Register a new user
        Returns: (success: bool, message: str)
        """
        # Validate username
        if not username or len(username.strip()) == 0:
            return False, "Username cannot be empty"
        
        username = username.strip().lower()
        
        # Check if username already exists
        if username in self.users:
            return False, "Username already exists. Please choose a different username."
        
        # Validate password
        if not password or len(password) < 4:
            return False, "Password must be at least 4 characters long"
        
        # Hash password and store user
        hashed_password = self._hash_password(password)
        self.users[username] = {
            "password": hashed_password
        }
        
        self._save_users()
        return True, "Registration successful! You can now log in."
    
    def login(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Authenticate user login
        Returns: (success: bool, message: str)
        """
        if not username or not password:
            return False, "Username and password cannot be empty"
        
        username = username.strip().lower()
        
        # Check if user exists
        if username not in self.users:
            return False, "Invalid username or password"
        
        # Verify password
        hashed_password = self._hash_password(password)
        if self.users[username]["password"] == hashed_password:
            return True, f"Welcome back, {username}!"
        else:
            return False, "Invalid username or password"
    
    def user_exists(self, username: str) -> bool:
        """Check if a user exists"""
        return username.lower() in self.users

