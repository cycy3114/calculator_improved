from calculator.calculations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(1, 0)
    except ZeroDivisionError:
        assert True
