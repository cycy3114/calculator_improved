import logging
from src.commands.add_command import AddCommand

def test_add_logs_info(caplog):
    with caplog.at_level(logging.INFO):
        AddCommand.execute(2, 2)
        assert "Adding 2 + 2 = 4" in caplog.text
