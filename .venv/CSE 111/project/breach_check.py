############################
# Colby Wilson
# 3/24/2025
# Password program (Breach)
###########################
import hashlib
import requests

def is_breached(password: str) -> bool:
    """
    Checks if a password has been breached using the Have I Been Pwned API.

    Args: 
        password (str): The password to check.

    Returns:
        bool: True if the password has been breached, False otherwise.
    """
    try:
        # Hashes the password
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        # Gets the first 5 characters of the SHA-1 hash
        prefix = sha1_password[:5]

        # Makes the request with a timeout of 5 seconds
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=8)

        # Checks if successful
        if response.status_code == 200:
            suffix = sha1_password[5:]
            return suffix in response.text
        else:
            return False
    except requests.exceptions.RequestException as e:
        # Catching request-specific exceptions
        print(f"An error occurred while making the request: {e}")
        return False
    except Exception as e:
        # Catching any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return False
