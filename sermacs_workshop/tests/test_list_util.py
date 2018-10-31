"""
Tests for list_util module
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop as acs
import pytest
import sys

def test_title_case():
    """Sample test, will always pass so long as import statement worked"""
    test_string = 'this IS a Test sTrinG'
    title_string = acs.title_case(test_string)
    print(title_string)
    assert title_string == 'This Is A Test String'
    return True

@pytest.mark.other
def test_type_failure():
    test_input = ['This','is','a','test']
    with pytest.raises(TypeError):
        acs.title_case(test_input)

@pytest.mark.skip
def test_empty_str():
    test_input = ''
    with pytest.raises(IndexError):
        acs.title_case(test_input)
