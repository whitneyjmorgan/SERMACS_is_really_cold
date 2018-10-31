"""
Tests for molssi_math module
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop as acs
import pytest
import sys

@pytest.mark.parametrize("num_list, expected_mean",[
([1,2,3,4,5],3.0),
([0,2,4,6],3),
([1,2,3,4],2.5),
])

def test_many(num_list,expected_mean):
    assert acs.mean(num_list) == expected_mean


# do all tests combinations of x with 0,1 and y with 2,3
# you cannot use ' quotes for these variables....
@pytest.mark.parametrize("x",[0,1])
@pytest.mark.parametrize("y",[2,3])
def test_foo(x,y):
    pass

@pytest.fixture
def num_list_3():
     return [1,2,3,4,5]

def test_mean_int(num_list_3):
    """Sample test, will always pass so long as import statement worked"""
    result = acs.mean(num_list_3)
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
    with pytest.raises(TypeError):
        acs.mean(test_data)

def test_type_failure():
    test_input = ' '
    with pytest.raises(TypeError):
        acs.mean(test_input)

def test_empty():
    test_input = []
    with pytest.raises(ZeroDivisionError):
        acs.mean(test_input)

#if you use pytest.raises(etc) you need to import pytest!
