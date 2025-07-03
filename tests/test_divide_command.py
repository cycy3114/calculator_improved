from src.commands.divide_command import DivideCommand
import pytest

def test_divide():
    assert DivideCommand.execute(12, 4) == 3.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        DivideCommand.execute(5, 0)
