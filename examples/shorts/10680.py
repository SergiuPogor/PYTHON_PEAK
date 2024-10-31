# Using collections.namedtuple for structured, immutable data handling

from collections import namedtuple

# Define a namedtuple for storing employee data
Employee = namedtuple("Employee", ["id", "name", "position", "salary"])

# Creating instances of Employee with named fields
emp1 = Employee(id=1, name="Alice Smith", position="Software Engineer", salary=85000)
emp2 = Employee(id=2, name="Bob Johnson", position="Data Scientist", salary=95000)

# Access data by field name for readability
print(f"{emp1.name} holds the position of {emp1.position} with a salary of ${emp1.salary}")
print(f"{emp2.name} holds the position of {emp2.position} with a salary of ${emp2.salary}")

# namedtuples are immutable - attempting to change a field will raise an error
try:
    emp1.salary = 90000
except AttributeError as e:
    print("Error:", e)

# Use namedtuple to unpack fields easily
id_, name, position, salary = emp1
print(f"Employee Unpacked: {name} with ID {id_} - {position} earning ${salary}")

# Convert to dictionary if mutable data structure is needed
emp_dict = emp1._asdict()  # Convert namedtuple to dict
emp_dict["salary"] = 88000  # Modify salary in dict
print("Updated employee data as dict:", emp_dict)