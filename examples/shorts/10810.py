# Example of implementing the Command Pattern in Python
class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Example usage
if __name__ == "__main__":
    # Create the light object
    living_room_light = Light()

    # Create command objects
    turn_on_command = TurnOnLightCommand(living_room_light)
    turn_off_command = TurnOffLightCommand(living_room_light)

    # Create a remote control
    remote = RemoteControl()

    # Turn on the light
    remote.set_command(turn_on_command)
    remote.press_button()  # Output: Light is ON

    # Turn off the light
    remote.set_command(turn_off_command)
    remote.press_button()  # Output: Light is OFF