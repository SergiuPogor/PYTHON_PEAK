class DynamicAttributes:
    def __init__(self, name):
        self.name = name
        self.age = 0  # Default age

    def update_attribute(self, attr_name, value):
        # Dynamically update the attribute
        setattr(self, attr_name, value)

# Create an instance of the class
person = DynamicAttributes("Alice")

# Print initial state
print(f"Before update: Name = {person.name}, Age = {person.age}")

# Update the age attribute dynamically
person.update_attribute('age', 30)

# Print updated state
print(f"After update: Name = {person.name}, Age = {person.age}")

# Update another attribute dynamically
person.update_attribute('job', 'Developer')

# Print to show new attribute
print(f"Job = {getattr(person, 'job')}")  # Output: Job = Developer