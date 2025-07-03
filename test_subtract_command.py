from src.commands.subtract_command import SubtractCommand

def test_subtract():
    assert SubtractCommand.execute(5, 3) == 2
