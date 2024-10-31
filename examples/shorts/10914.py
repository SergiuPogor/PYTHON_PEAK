# Quick Complex Sorting Using Lambda in Python

# List of employees with nested details
employees = [
    {"name": "Alice", "department": "Engineering", "performance": {"projects": 7, "satisfaction": 3.9}},
    {"name": "Bob", "department": "Sales", "performance": {"projects": 5, "satisfaction": 4.5}},
    {"name": "Eve", "department": "Marketing", "performance": {"projects": 6, "satisfaction": 4.2}},
    {"name": "John", "department": "Engineering", "performance": {"projects": 8, "satisfaction": 4.0}},
    {"name": "Alice", "department": "Sales", "performance": {"projects": 10, "satisfaction": 3.7}}
]

# Sort by department, then by satisfaction score in performance
sorted_employees = sorted(
    employees,
    key=lambda x: (x["department"], x["performance"]["satisfaction"]),
    reverse=True
)

print("Sorted Employees:")
for emp in sorted_employees:
    print(emp)