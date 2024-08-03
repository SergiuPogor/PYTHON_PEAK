class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"{self.name}: ${self.salary}"

# List of employee objects
employees = [
    Employee("Alice", 90000),
    Employee("Bob", 80000),
    Employee("Charlie", 95000)
]

# Find employee with the highest salary
highest_paid = max(employees, key=lambda e: e.salary)
print("Highest paid employee:", highest_paid)