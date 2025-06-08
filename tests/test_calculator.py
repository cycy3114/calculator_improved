"""Test calculator operations."""
from calculator.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
