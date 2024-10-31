from typing import Callable, Dict

# Command pattern using callable objects
class Command:
    def __init__(self, execute: Callable, undo: Callable = None):
        self.execute = execute
        self.undo = undo

class RemoteControl:
    def __init__(self):
        self.commands: Dict[str, Command] = {}
    
    def register_command(self, name: str, command: Command):
        self.commands[name] = command

    def execute_command(self, name: str):
        command = self.commands.get(name)
        if command:
            command.execute()
        else:
            print(f"Command '{name}' not found.")

    def undo_command(self, name: str):
        command = self.commands.get(name)
        if command and command.undo:
            command.undo()

# Usage
def turn_on_lights():
    print("Lights are ON")

def turn_off_lights():
    print("Lights are OFF")

# Creating commands
light_on = Command(turn_on_lights, turn_off_lights)
light_off = Command(turn_off_lights, turn_on_lights)

# Registering commands
remote = RemoteControl()
remote.register_command("light on", light_on)
remote.register_command("light off", light_off)

# Executing and undoing commands
remote.execute_command("light on")
remote.undo_command("light on")
remote.execute_command("light off")