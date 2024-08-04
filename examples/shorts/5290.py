# Example of using property() to control access to class attributes

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def is_adult(self):
        return self._age >= 18

# Create an instance of Person
person = Person("Alice", 30)

# Access and modify attributes using properties
print(person.name)          # Output: Alice
print(person.is_adult)     # Output: True

person.name = "Bob"         # Update name
print(person.name)          # Output: Bob

try:
    person.age = -5         # Attempt to set invalid age
except ValueError as e:
    print(e)                # Output: Age cannot be negative