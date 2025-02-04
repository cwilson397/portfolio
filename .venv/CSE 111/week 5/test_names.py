#########################################
# Test_names.py
# February 2nd, 2025
# Colby Wilson
# CSE 111
##########################################

from names import make_full_name, extract_family_name, extract_given_name
import pytest

# Test for the make_full_name function
def test_make_full_name():
    # Test cases for different types of names
    assert make_full_name("John", "Doe") == "John Doe"
    assert make_full_name("Jane", "Smith") == "Jane Smith"
    assert make_full_name("Mary", "Johnson") == "Mary Johnson"
    assert make_full_name("Jean-Paul", "Belmondo") == "Jean-Paul Belmondo"  # Hyphenated names
    assert make_full_name("Avery", "Longlastname") == "Avery Longlastname"  # Long names

# Test for the extract_family_name function
def test_extract_family_name():
    # Test cases for extracting the family name from full names
    assert extract_family_name("John Doe") == "Doe"
    assert extract_family_name("Jane Smith") == "Smith"
    assert extract_family_name("Jean-Paul Belmondo") == "Belmondo"  # Hyphenated family name
    assert extract_family_name("Avery Longlastname") == "Longlastname"  # Long family name

# Test for the extract_given_name function
def test_extract_given_name():
    # Test cases for extracting the given name from full names
    assert extract_given_name("John Doe") == "John"
    assert extract_given_name("Jane Smith") == "Jane"
    assert extract_given_name("Jean-Paul Belmondo") == "Jean-Paul"  # Hyphenated given name
    assert extract_given_name("Avery Longlastname") == "Avery"  # Long given name

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
