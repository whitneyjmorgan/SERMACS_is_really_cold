"""
Tests for molssi_math module
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop as acs
import pytest
import sys

def test_mean_int():
    """Sample test, will always pass so long as import statement worked"""
    test_data = [1,2,3,4,5]
    result = acs.mean(test_data)
    assert result == 3.0
    return True

def test_mean_float():
    """Sample test, will always pass so long as import statement worked"""
    test_data = [1.0,2.0,3.0,4.0,5.0]
    result = acs.mean(test_data)
    assert result == 3.0
    return True

def test_mean_mixed():
    """Sample test, will always pass so long as import statement worked"""
    test_data = [1.0,2,3.0,4.0,5.0]
    result = acs.mean(test_data)
    assert result == 3.0
    return True

def test_mixed_failure():
    test_data = [1.0,'2',3.0,4.0,5.0]
    result = acs.mean(test_data)
    with pytest.raises(TypeError):
        acs.mean(test_input)

def test_type_failure():
    test_input = ' '
    with pytest.raises(TypeError):
        acs.mean(test_input)

def test_empty():
    test_input = []
    with pytest.raises(ZeroDivisionError):
        acs.mean(test_input)

#if you use pytest.raises(etc) you need to import pytest!
