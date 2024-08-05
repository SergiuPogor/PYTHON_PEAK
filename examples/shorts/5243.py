class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        info = f"Name: {self.name}, Age: {self.age}"
        if hasattr( self, 'email'):
            info += f", Email: {self.email}"
        print(info)

# Create a Person object
person = Person("John Doe", 30, "john.doe@example.com")
person.display_info()

# Dynamically delete the 'email' attribute
delattr(person, 'email')
person.display_info()

# Attempting to delete a non-existing attribute
try:
    delattr(person, 'phone')
except AttributeError as e:
    print(f"Error: {e}")

# Dynamically add an attribute and then delete it
person.phone = "123-456-7890"
print(f"Phone before deletion: {person.phone}")
delattr(person, 'phone')
print(f"Has phone attribute: {'phone' in person.__dict__}")

# Advanced example: Deleting multiple attributes dynamically
attributes_to_delete = ['name', 'age']
for attr in attributes_to_delete:
    if hasattr(person, attr):
        delattr(person, attr)

# Check which attributes remain
remaining_attributes = person.__dict__.keys()
print(f"Remaining attributes: {list(remaining_attributes)}")



