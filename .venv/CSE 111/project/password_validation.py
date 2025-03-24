############################
# Colby Wilson
# 3/24/2025
# Password program (Validate)
###########################

import re

def is_valid_length(password: str) -> bool:
    """
    Checks if the given password has a minimum length of 8 characters.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password length is at least 8 characters, False otherwise.
    """
    return len(password) >= 8

def has_uppercase(password: str) -> bool:
    """
    Checks if the given password contains at least one uppercase letter.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains at least one uppercase letter, False otherwise.
    """
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password: str) -> bool:
    """
    Checks if the given password contains at least one lowercase letter.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains at least one lowercase letter, False otherwise.
    """
    return bool(re.search(r'[a-z]', password))

def has_digit(password: str) -> bool:
    """
    Checks if the given password contains at least one digit.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains at least one digit, False otherwise.
    """
    return bool(re.search(r'\d', password))

def has_special_char(password: str) -> bool:
    """
    Checks if the given password contains at least one special character.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains at least one special character, False otherwise.
    """
    return bool(re.search(r'[\W_]', password))

def check_password_strength(password: str) -> str:
    """
    Checks the overall strength of the given password based on length,
    uppercase letters, lowercase letters, digits, and special characters.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating whether the password is strong or what requirements are missing.
    """
    if not is_valid_length(password):
        return "Password is too short"
    if not has_uppercase(password):
        return "Password needs at least one uppercase letter"
    if not has_lowercase(password):
        return "Password needs at least one lowercase letter"
    if not has_digit(password):
        return "Password needs at least one number"
    if not has_special_char(password):
        return "Password needs at least one special character"
    return "Password is strong"
