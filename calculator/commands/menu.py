class MenuCommand:
    def __init__(self, command_manager):
        self.command_manager = command_manager

    def execute(self):
        return "Available commands:\n" + "\n".join(
            f"{str(cmd)}" for cmd in self.command_manager.commands.values()
        )
    
    def __str__(self):
        return "menu - Shows available commands"
