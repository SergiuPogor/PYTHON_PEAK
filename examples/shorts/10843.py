from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def get_color_name(color):
    if color == Color.RED:
        return "Red Color"
    elif color == Color.GREEN:
        return "Green Color"
    elif color == Color.BLUE:
        return "Blue Color"
    return "Unknown Color"

# Example usage
def main():
    color_choice = Color.GREEN
    print(f"You selected: {get_color_name(color_choice)}")

if __name__ == "__main__":
    main()