# Example of using object() for dynamic attribute assignment

# Create a basic object with no attributes
dynamic_obj = object()

# Create a wrapper class to allow dynamic attribute assignment
class DynamicObject:
    def __init__(self):
        self.__dict__ = {}

# Instantiate the dynamic object
dyn_obj = DynamicObject()

# Dynamically add attributes to the object
dyn_obj.name = "John Doe"
dyn_obj.age = 30
dyn_obj.is_active = True

# Access the dynamically added attributes
print(f"Name: {dyn_obj.name}")  # Output: Name: John Doe
print(f"Age: {dyn_obj.age}")    # Output: Age: 30
print(f"Is Active: {dyn_obj.is_active}")  # Output: Is Active: True

# Modify attributes
dyn_obj.age = 31
print(f"Updated Age: {dyn_obj.age}")  # Output: Updated Age: 31

# Use the object in a function
def describe_person(person):
    return f"Name: {person.name}, Age: {person.age}, Active: {person.is_active}"

print(describe_person(dyn_obj))  # Output: Name: John Doe, Age: 31, Active: True