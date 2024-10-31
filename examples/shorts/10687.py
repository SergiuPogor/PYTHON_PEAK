from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def describe_color(color):
    # Ensure color is an instance of Color
    if not isinstance(color, Color):
        raise ValueError("Invalid color")
    return f"The color is {color.name} with value {color.value}"

def main():
    # Example usage of enum
    for color in Color:
        print(describe_color(color))

# Run the main function
main()