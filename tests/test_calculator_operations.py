import pytest
from calculator.calculation import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_multiply():
    assert Calculator.multiply(3, 4) == 12

def test_divide():
    assert Calculator.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

def test_history():
    # Clear history for testing
    Calculator.history.clear()
    Calculator.add(1, 1)
    Calculator.subtract(2, 1)
    history = Calculator.get_history()
    assert len(history) == 2
    assert "Added 1 + 1 = 2" in history[0]