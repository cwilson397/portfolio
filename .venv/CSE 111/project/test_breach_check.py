##################################
# 3/31/2025
# Password Breach Check Test
# Colby Wilson
##################################

import pytest
from breach_check import is_breached

# Test the breach check
def test_is_breached():
    """Test if a password is in the breach database"""
    # Replace with a known breached password for testing
    breached_password = "123456"
    non_breached_password = "unique_password123"

    print("Testing breached password:")
    result_breached = is_breached(breached_password)
    print(f"Result for {breached_password}: {result_breached}")
    assert result_breached is True  # This should return True

    print("Testing non-breached password:")
    result_non_breached = is_breached(non_breached_password)
    print(f"Result for {non_breached_password}: {result_non_breached}")
    assert result_non_breached is False  # This should return False

# Calls pytest to run tests when executing this script directly
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
