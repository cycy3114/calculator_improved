"""Test module for calculator operations with parameterized data."""
import pytest
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.mark.parametrize("first_num,second_num,operation,expected", [
    (10, 5, "add", 15),
    (10, 5, "subtract", 5),
    (10, 5, "multiply", 50),
    (10, 5, "divide", 2),
    (0.1, 0.2, "add", 0.3),  # Floating point test

    # Error cases
    (10, 0, "divide", "Error: Cannot divide by zero"),
    (10, "first_num", "add", "Error: Invalid numbers provided"),
    ("x", 5, "multiply", "Error: Invalid numbers provided"),
    (10, 5, "power", "Error: Unknown operation"),  # Invalid operation

    # Edge cases
    (999999999, 1, "add", 1000000000),  # Large numbers (fixed expected value)
    (0, 0, "add", 0),  # Zero cases
])
def test_calculator_operations(first_num, second_num, operation, expected):
    """Test calculator operations with dynamically generated data.

    Args:
        first_num: First test number
        second_num: Second test number
        operation: Math operation to test
        expected: Expected result
    """
    calc = Calculator()

    if isinstance(expected, str) and expected.startswith("Error:"):
        # Test for expected error cases
        with pytest.raises(ValueError, match=expected[7:]):
            calc.calculate(operation, first_num, second_num)
    else:
        # Test normal operations with precise decimal comparison
        result = calc.calculate(operation, first_num, second_num)
        assert Decimal(str(result)).quantize(Decimal('1.00000000')) == \
               Decimal(str(expected)).quantize(Decimal('1.00000000'))
# Additional command-specific tests
@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 5),
    (0, 0, 0),
    (-1, 1, -2),
    (1.5, 0.5, 1.0),
    ("10", 5, 5),
])
def test_subtract_command(a, b, expected):
    """Test SubtractCommand directly"""
    assert SubtractCommand().execute(a, b) == expected

def test_menu_command():
    """Test MenuCommand output"""
    from calculator.commands.menu import MenuCommand
    from calculator.calculator import CommandManager

    manager = CommandManager()
    menu = MenuCommand(manager)
    output = menu.execute()

    assert "add" in output
    assert "subtract" in output
    assert "divide" in output
    assert "Available commands" in output

def test_repl_interface(monkeypatch):
    """Test REPL exit command"""
    monkeypatch.setattr('builtins.input', lambda _: "exit")
    calc = Calculator()
    calc.start_repl()
# Test Calculator class directly
def test_calculator_initialization():
    calc = Calculator()
    assert 'add' in calc.command_manager.commands
    assert 'menu' in calc.command_manager.commands

# Test command loading
def test_unknown_operation():
    calc = Calculator()
    with pytest.raises(ValueError, match="Unknown operation"):
        calc.calculate("invalid_op", 1, 1)

# Menu command tests
def test_menu_command_execution():
    from calculator.commands.menu import MenuCommand
    cmd = MenuCommand(Calculator().command_manager)
    assert "Available commands" in cmd.execute()
    assert "add" in cmd.execute()

# Edge cases for subtraction
@pytest.mark.parametrize("a,b,expected", [
    (1.111, 0.111, 1.0),  # Decimal precision
    (-5, -3, -2),  # Negative numbers
    (0, -5, 5),  # Zero handling
])
def test_subtract_edge_cases(a, b, expected):
    from calculator.commands.subtract import SubtractCommand
    assert SubtractCommand().execute(a, b) == pytest.approx(expected)
# Test REPL interactions
def test_repl_unknown_command(capsys):
    calc = Calculator()
    calc.start_repl_input("invalid_command\n")  # You'll need to implement this helper
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_repl_help_command(capsys):
    calc = Calculator()
    calc.start_repl_input("menu\n")
    captured = capsys.readouterr()
    assert "Available commands" in captured.out
# Test calculator.py's REPL thoroughly
def test_repl_division_by_zero(capsys):
    calc = Calculator()
    calc.start_repl_input("divide 10 0\nexit\n")
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

# Test menu command display
def test_menu_command_display():
    from calculator.commands.menu import MenuCommand
    cmd = MenuCommand(Calculator().command_manager)
    menu_text = cmd.execute()
    assert "add" in menu_text
    assert "subtract" in menu_text
    assert "multiply" in menu_text
    assert "divide" in menu_text

# Test plugin loading
def test_plugin_loading(tmp_path):
    plugin_code = """
def register(commands):
    commands['square'] = lambda x: x*x
"""
    plugin_file = tmp_path / "square_plugin.py"
    plugin_file.write_text(plugin_code)
    
    calc = Calculator()
    assert 'square' in calc.command_manager.commands
    assert calc.calculate("square", 4) == 16
