from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

def get_color_name(color):
    if not isinstance(color, Color):
        raise ValueError("Invalid color type")
    return color.name

def main():
    selected_color = Color.RED
    print(f"Selected color is: {get_color_name(selected_color)}")
    
    # Using enum to prevent invalid values
    try:
        invalid_color = 4  # This should not be allowed
        print(get_color_name(invalid_color))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()