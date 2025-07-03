from src.commands.divide_command import DivideCommand
import pytest

def test_divide():
    assert DivideCommand.execute(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        DivideCommand.execute(10, 0)
