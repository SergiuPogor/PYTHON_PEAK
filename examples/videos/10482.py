class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when there is a validation error."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when an item is not found."""
    def __init__(self, item):
        self.item = item
        self.message = f"{item} not found."
        super().__init__(self.message)

def validate_user_input(user_input):
    if not isinstance(user_input, str):
        raise ValidationError("Input must be a string.")
    if len(user_input) == 0:
        raise ValidationError("Input cannot be empty.")

def find_item_in_list(item, items):
    if item not in items:
        raise NotFoundError(item)

def main():
    items = ["apple", "banana", "orange"]
    
    user_input = "grape"
    try:
        validate_user_input(user_input)
        find_item_in_list(user_input, items)
    except CustomError as e:
        print(f"Error occurred: {e}")

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()