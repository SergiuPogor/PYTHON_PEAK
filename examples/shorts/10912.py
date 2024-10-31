# Complex sorting example using sorted() with a lambda function

# Data: A list of dictionaries representing employees with mixed criteria
employees = [
    {"name": "Alice", "department": "Engineering", "salary": 95000, "years_with_company": 3},
    {"name": "Bob", "department": "Marketing", "salary": 75000, "years_with_company": 5},
    {"name": "Carol", "department": "Engineering", "salary": 120000, "years_with_company": 7},
    {"name": "Dan", "department": "Marketing", "salary": 95000, "years_with_company": 2},
    {"name": "Eve", "department": "Sales", "salary": 65000, "years_with_company": 1}
]

# Sort employees by department, then by descending salary, then by years with company
sorted_employees = sorted(
    employees,
    key=lambda x: (x["department"], -x["salary"], x["years_with_company"])
)

for employee in sorted_employees:
    print(employee)