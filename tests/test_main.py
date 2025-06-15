from main import handle_user_input

def test_valid_add():
    assert handle_user_input("5", "3", "add") == "The result of 5 add 3 is equal to 8"

def test_invalid_input():
    assert handle_user_input("a", "3", "add") == "Invalid number input: a or 3 is not a valid number."

def test_unknown_operation():
    assert handle_user_input("5", "3", "mod") == "Unknown operation: mod"

def test_divide_by_zero():
    assert handle_user_input("10", "0", "divide") == "An error occurred: Cannot divide by zero"
