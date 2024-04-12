"""Simple test module providing test for my previous function"""
from calculator import addition, soustraction, division


def test_addition():
    """Simple test function on addition"""
    assert addition(1, 2) == 3

def test_soustraction():
    """Simple test function on soustraction"""
    assert soustraction(2,1) == 1

def test_division():
    """Simple test function on division"""
    assert division(6,2) == 3