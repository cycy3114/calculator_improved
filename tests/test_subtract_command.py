from src.commands.subtract_command import SubtractCommand

def test_subtract():
    assert SubtractCommand.execute(10, 4) == 6
