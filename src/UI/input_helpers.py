"""
Input helpers and validators for UI layer
Reusable functions for collecting and validating user input
"""
import datetime
from typing import Tuple


def get_required_input(prompt: str) -> str:
    """
    Get a required (non-empty) input from the user.
    Keeps prompting until a non-empty value is entered.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required.")


def get_date_input(prompt: str) -> str:
    """
    Get a date input in YYYY-MM-DD format.
    Validates format and ensures it's a valid date.
    """
    while True:
        date_str = input(prompt).strip()
        if validate_date_format(date_str):
            return date_str
        print("Invalid date format. Use YYYY-MM-DD (e.g., 2025-12-25)")


def validate_date_format(date_str: str) -> bool:
    """
    Validate that a string is in YYYY-MM-DD format and represents a valid date.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_3_day_duration(start_date_str: str, end_date_str: str) -> Tuple[bool, str]:
    """
    Validate that the tournament duration is exactly 3 days.
    end_date must be exactly start_date + 2 days.
    
    Returns:
        (True, "") if valid
        (False, error_message) if invalid
    """
    try:
        start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."
    
    duration = (end - start).days
    if duration != 2:
        return False, f"Tournament must be exactly 3 days long (end date = start date + 2). Current duration: {duration + 1} days."
    
    return True, ""


def get_email_input(prompt: str) -> str:
    """
    Get an email input with basic validation.
    Just checks for @ symbol and a dot after it.
    """
    while True:
        email = input(prompt).strip()
        if email and "@" in email and "." in email.split("@")[1]:
            return email
        print("Invalid email format. Please include @ and a domain.")


def get_phone_input(prompt: str) -> str:
    """
    Get a phone number input.
    For now, just ensures it's not empty - can add more validation later.
    """
    return get_required_input(prompt)


def confirm_action(prompt: str) -> bool:
    """
    Ask user for confirmation (yes/no).
    Returns True for yes, False for no.
    """
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Please enter 'y' for yes or 'n' for no.")
