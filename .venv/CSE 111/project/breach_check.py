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
        # Hashes the password using SHA1
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        # Gets the first 5 characters of the SHA-1 hash
        prefix = sha1_password[:5]

        # Makes the request with a timeout of 5 seconds
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=5)

        # If the request is successful, check if the suffix is in the response
        if response.status_code == 200:
            # The API returns a list of hash suffixes
            suffix = sha1_password[5:]

            # Check if the suffix is present in the response text (matching the case)
            return any(suffix == line.split(":")[0] for line in response.text.splitlines())

        # If the response code is not 200, return False
        return False

    except requests.exceptions.RequestException as e:
        # Catching request-specific exceptions (e.g., network errors)
        print(f"An error occurred while making the request: {e}")
        return False
    except Exception as e:
        # Catching any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return False
