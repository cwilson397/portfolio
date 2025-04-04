##################################
# 3/31/2025
# Password Generation Test
# Colby Wilson
##################################

import pytest
from password_generation import generate_strong_password

# Test password length constraints
def test_generate_password_length():
    """Tests if the generated password is within the allowed length (8-20)."""
    assert 8 <= len(generate_strong_password(8)) <= 20
    assert 8 <= len(generate_strong_password(12)) <= 20
    assert 8 <= len(generate_strong_password(20)) <= 20
    assert len(generate_strong_password(5)) == 8  # Should default to 8
    assert len(generate_strong_password(25)) == 20  # Should default to 20

# Test if generated password contains required character types
def test_generate_password_character_types():
    """Tests if the generated password contains at least one uppercase, lowercase, digit, and special character."""
    password = generate_strong_password(16)
    
    assert any(c.isupper() for c in password)  # At least one uppercase letter
    assert any(c.islower() for c in password)  # At least one lowercase letter
    assert any(c.isdigit() for c in password)  # At least one digit
    assert any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)  # At least one special character

# Calls pytest to run tests when executing this script directly
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
