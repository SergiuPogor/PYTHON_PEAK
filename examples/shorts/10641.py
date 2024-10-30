from collections import namedtuple
from datetime import datetime

# Define a namedtuple for Employee with basic fields
Employee = namedtuple("Employee", ["id", "name", "position", "start_date", "salary"])

# Create employee records with namedtuples
employees = [
    Employee(id=101, name="Alice", position="Data Engineer", start_date="2022-03-01", salary=75000),
    Employee(id=102, name="Bob", position="Backend Developer", start_date="2021-06-15", salary=80000),
    Employee(id=103, name="Charlie", position="Product Manager", start_date="2023-01-20", salary=95000),
]

# Display employee details, leveraging namedtuple's readability
for employee in employees:
    print(f"{employee.name}, {employee.position}: ${employee.salary} started on {employee.start_date}")

# Calculate years of experience using namedtuple data
def years_of_experience(employee: Employee):
    start = datetime.strptime(employee.start_date, "%Y-%m-%d")
    return (datetime.now() - start).days // 365

# Add the years of experience to the output for each employee
for employee in employees:
    experience = years_of_experience(employee)
    print(f"{employee.name} has {experience} years of experience.")

# Example output:
# Alice, Data Engineer: $75000 started on 2022-03-01
# Bob, Backend Developer: $80000 started on 2021-06-15
# Charlie, Product Manager: $95000 started on 2023-01-20
# Alice has 2 years of experience.
# Bob has 3 years of experience.
# Charlie has 1 year of experience.