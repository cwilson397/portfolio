############################
# Colby Wilson
# 3/24/2025
# Password program (Generator)
###########################

import random
import string

def generate_strong_password(length: int) -> str:
    """
    Generates a strong password with a specified length.

    The password will consist of random uppercase letters, lowercase letters, digits, 
    and special characters. The length is clamped between 8 and 20 characters.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.
    """
    # Clamp the length to be between 8 and 20 characters
    if length < 8:
        length = 8
    elif length > 20:
        length = 20

    # Generate a random password using the allowed characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
