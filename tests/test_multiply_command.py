from src.commands.multiply_command import MultiplyCommand

def test_multiply():
    assert MultiplyCommand.execute(6, 7) == 42
