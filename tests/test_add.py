from src.commands.add_command import AddCommand

def test_add_command():
    assert AddCommand.execute(2, 3) == 5
