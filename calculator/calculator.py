from importlib import import_module
from pathlib import Path
from .commands import *

class CommandManager:
    def __init__(self):
        self.commands = {}
        self._load_commands()
        self._load_plugins()

    def _load_commands(self):
        self.commands['add'] = AddCommand()
        self.commands['subtract'] = SubtractCommand()
        self.commands['multiply'] = MultiplyCommand()
        self.commands['divide'] = DivideCommand()
        self.commands['menu'] = MenuCommand(self)

    def _load_plugins(self):
        plugins_dir = Path(__file__).parent.parent / "plugins"
        for file in plugins_dir.glob("*.py"):
            if file.name.startswith("_"):
                continue
            module_name = f"plugins.{file.stem}"
            try:
                module = import_module(module_name)
                if hasattr(module, "register"):
                    module.register(self.commands)
            except ImportError as e:
                print(f"Failed to load plugin {file.name}: {e}")

class Calculator:
    def __init__(self):
        self.command_manager = CommandManager()

    def calculate(self, operation, a, b):
        if operation not in self.command_manager.commands:
            raise ValueError(f"Unknown operation: {operation}")
        return self.command_manager.commands[operation].execute(a, b)

    def start_repl(self):
        print("Calculator REPL. Type 'menu' for commands or 'exit' to quit.")
        while True:
            try:
                user_input = input(">>> ").strip()
                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'quit']:
                    break

                parts = user_input.split()
                command_name = parts[0].lower()

                if command_name == 'menu':
                    print(self.command_manager.commands['menu'].execute())
                    continue

                if command_name not in self.command_manager.commands:
                    print(f"Unknown command: {command_name}")
                    continue

                try:
                    args = parts[1:]
                    if len(args) != 2:
                        print(f"Usage: {command_name} <num1> <num2>")
                        continue

                    result = self.command_manager.commands[command_name].execute(*args)
                    print(result)
                except Exception as e:
                    print(f"Error: {e}")

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break
