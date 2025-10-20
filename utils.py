"""
Utility Functions
Helper functions for the application
"""

import os
import platform


def clear_screen():
    """Clear the terminal screen"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def print_header(text: str, width: int = 60):
    """Print a formatted header"""
    print("\n" + "=" * width)
    print(text.center(width))
    print("=" * width)


def print_separator(width: int = 60):
    """Print a separator line"""
    print("-" * width)


def get_input(prompt: str, input_type=str, allow_empty=False):
    """
    Get validated input from user
    
    Args:
        prompt: The prompt to display
        input_type: The type to convert input to (str, int, float)
        allow_empty: Whether to allow empty input
    
    Returns:
        The validated input value or None if cancelled
    """
    while True:
        try:
            value = input(prompt).strip()
            
            if not value:
                if allow_empty:
                    return None
                print("Input cannot be empty. Please try again.")
                continue
            
            if input_type == str:
                return value
            elif input_type == int:
                return int(value)
            elif input_type == float:
                return float(value)
            else:
                return value
                
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled.")
            return None


def confirm_action(prompt: str = "Are you sure?") -> bool:
    """
    Ask user to confirm an action
    
    Returns:
        True if confirmed, False otherwise
    """
    while True:
        response = input(f"{prompt} (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def pause():
    """Pause and wait for user to press Enter"""
    input("\nPress Enter to continue...")

