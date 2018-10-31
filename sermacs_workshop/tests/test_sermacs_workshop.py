"""
Unit and regression test for the sermacs_workshop package.
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop
import pytest
import sys

def test_sermacs_workshop_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sermacs_workshop" in sys.modules

def test_whatever():
    """Sample test, will always pass so long as import statement worked"""
    a = 1
    b = 2
    assert a+b==3
