class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

def process_object(obj):
    if isinstance(obj, Employee):
        print(f"Employee: {obj.name}, ID: {obj.employee_id}")
    elif isinstance(obj, Person):
        print(f"Person: {obj.name}")
    else:
        print("Unknown type")

# Example usage
p = Person("John Doe")
e = Employee("Jane Smith", 12345)

process_object(p)  # Output: Person: John Doe
process_object(e)  # Output: Employee: Jane Smith, ID: 12345