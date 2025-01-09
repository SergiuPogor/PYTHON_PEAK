class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize the name attribute
        self.age = age    # Initialize the age attribute

    def __setattr__(self, key, value):
        if key == 'age':
            if value < 0:
                raise ValueError("Age cannot be negative.")
        # Allow any other attribute to be set without restrictions
        super().__setattr__(key, value)

# Example usage
def main():
    try:
        john = Person("John Doe", 30)
        print(f"Name: {john.name}, Age: {john.age}")
        
        # This will work
        john.age = 35
        print(f"Updated Age: {john.age}")

        # This will raise a ValueError
        john.age = -5
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# The __setattr__ method in this class ensures that age 
# cannot be set to a negative number, thus maintaining 
# data integrity within the Person class.