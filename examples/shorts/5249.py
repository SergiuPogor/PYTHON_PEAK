# Example of using getattr() for dynamic attribute access

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

# Creating an instance of Person
person = Person("Alice", 30)

# Dynamic attribute access using getattr()
attribute_name = "name"
attribute_value = getattr(person, attribute_name, "Attribute not found")
print(f"Value of '{attribute_name}': {attribute_value}")

# Accessing a method dynamically
method_name = "greet"
greeting = getattr(person, method_name, lambda: "Method not found")()
print(f"Greeting: {greeting}")

# Handling a non-existent attribute
non_existent_attr = getattr(person, "non_existent", "Default Value")
print(f"Non-existent attribute: {non_existent_attr}")

# Use case: dynamically setting attributes
setattr(person, "occupation", "Engineer")
print(f"Occupation: {getattr(person, 'occupation')}")
