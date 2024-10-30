# Example of using a metaclass to enforce constraints in Python

# Define a metaclass
class ConstraintMeta(type):
    def __new__(cls, name, bases, attrs):
        # Enforce a rule that every class must have a 'name' attribute
        if 'name' not in attrs:
            raise ValueError(f"{name} must have a 'name' attribute")
        return super().__new__(cls, name, bases, attrs)

# Create classes using the metaclass
class ValidClass(metaclass=ConstraintMeta):
    name = "I am valid"

class InvalidClass(metaclass=ConstraintMeta):
    # This will raise an error because 'name' is missing
    pass

def main():
    valid_instance = ValidClass()
    print(f"Created: {valid_instance.name}")

if __name__ == "__main__":
    main()