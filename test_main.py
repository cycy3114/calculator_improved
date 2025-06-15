from main import handle_user_input

def test_valid_operations():
    assert handle_user_input("5", "3", "add") == "The result of 5.0 add 3.0 is equal to 8.0"
    assert handle_user_input("10", "2", "subtract") == "The result of 10.0 subtract 2.0 is equal to 8.0"

def test_invalid_input():
    assert "Invalid number input" in handle_user_input("a", "3", "add")
    assert "Unknown operation" in handle_user_input("5", "3", "modulus")
