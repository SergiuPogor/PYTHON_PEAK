import json

# Custom encoder class
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # Check if the object is of a specific type
        if isinstance(obj, set):
            # Convert set to a list
            return list(obj)
        if hasattr(obj, 'to_dict'):
            # If the object has a to_dict method, call it
            return obj.to_dict()
        # Let the base class default method raise the TypeError
        return super().default(obj)

# Example class to encode
class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = set(hobbies)

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'hobbies': self.hobbies
        }

# Create an instance of Person
person = Person("Alice", 30, ["reading", "hiking", "coding"])

# Use the custom encoder to convert the person object to JSON
json_output = json.dumps(person, cls=CustomJSONEncoder, indent=4)

# Display the JSON output
print(json_output)

# Example with a nested object
class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees  # List of Person objects

    def to_dict(self):
        return {
            'name': self.name,
            'employees': [emp.to_dict() for emp in self.employees]
        }

# Create a company with employees
company = Company("Tech Solutions", [person, Person("Bob", 25, ["gaming", "music"])])

# Convert the company object to JSON
json_company_output = json.dumps(company, cls=CustomJSONEncoder, indent=4)

# Display the company JSON output
print(json_company_output)