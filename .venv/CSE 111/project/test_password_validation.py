##################################
# 3/31/2025
# Password Validation Test
# Colby Wilson
##################################

import pytest
from password_validation import (
    is_valid_length,
    has_uppercase,
    has_lowercase,
    has_digit,
    has_special_char,
    check_password_strength
)

# Testing the passowrd length
def test_is_valid_length():
    """ A function to test the is_valid_length function"""
    assert is_valid_length("12345678") is True
    assert is_valid_length("short") is False

# Test for uppercase letters
def test_has_uppercase():
    """ A Function to test the has_uppercase function"""
    assert has_uppercase("Password") is True
    assert has_uppercase("password") is False

# Test for lowercase letters
def test_has_lowercase():
    """ A Function to test the has_lowercase function"""
    assert has_lowercase("PassWord") is True
    assert has_lowercase("PASSWORD") is False

# Test for digits
def test_has_digit():
    """ A Function to test the has_digit function"""
    assert has_digit("Password1") is True
    assert has_digit("NoDigitsHere") is False

# Test for special characters
def test_has_special_char():
    """ A Function testing for all special Characters"""
    assert has_special_char("Pass@word") is True  # Contains '@', should pass
    assert has_special_char("NoSpecialChars") is False  # No special chars, should fail
    assert has_special_char("Test#ing!") is True  # Contains '#' and '!', should pass
    assert has_special_char("123$456") is True  # Contains '$', should pass
    assert has_special_char("NormalText.") is True  # Contains '.', should pass
    assert has_special_char("JustLettersAndNumbers123") is False  # No special chars, should fail

# Test password strength check
def test_check_password_strength():
    """ Final Culmination, it double checks everything."""
    assert check_password_strength("Weak") == "Password is too short"
    assert check_password_strength("weakpassword") == "Password needs at least one uppercase letter"
    assert check_password_strength("WeakPassword") == "Password needs at least one number"
    assert check_password_strength("WeakPassword1") == "Password needs at least one special character"
    assert check_password_strength("Str0ng@Password") == "Password is strong"

# Calls functions for running program manually
pytest.main(["-v", "--tb=line", "-rN", __file__])
