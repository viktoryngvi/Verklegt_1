import os
import platform

"""
Input helper for the functions in the UI modules
only to validate basic inputs for example empty inputs or integer inputs
so that the program does not crash on invalid inputs and will deliver an error message instead.
"""

def get_non_empty_input(prompt: str) -> str:
    """Get input that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty.")


def get_integer_input(prompt: str) -> int:
    """Get a valid integer."""
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Error: Please enter a number.")


def get_choice_input(prompt: str, valid_choices: list) -> str:
    """Get one of the allowed choices."""
    valid = [str(c) for c in valid_choices]
    
    while True:
        value = input(prompt).strip()
        if value in valid:
            return value
        print("Invalid choice. Try again.")


def get_optional_input(prompt: str) -> str:
    """Get input that can be empty (returns empty string if nothing entered)."""
    return input(prompt).strip()

# prompt takes the user prompt, and the items is set to a variable list that is called from the LL wrapper
def choose_from_list(prompt: str, items: list):
    """Display numbered list and let user choose one item."""
    for i, item in enumerate(items, start=1):
        print(f"  [{i}] {item}")
    print("")
    idx = get_integer_input(prompt) - 1
    return items[idx]


def clear_screen():
    """Clear the screen between menus
        the function works different on windows and mac/linux
        so first check what OS the program is running on then use the correct command"""
    
    if platform.system() == "Windows":
        # cls means clearing the screen 
        os.system("cls")
    else:
        # on mac and linux use clear command to clear the screen
        os.system("clear")

