# Practical use of filter() in a real-world scenario

# Example: Filtering out even numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(num):
    return num % 2 != 0

odd_numbers = list(filter(is_odd, numbers))
print(f"Odd numbers: {odd_numbers}")

# Example: Filtering out employees older than 30 from a list of dictionaries

employees = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 28},
    {"name": "Diana", "age": 40}
]

def is_under_30(employee):
    return employee["age"] < 30

young_employees = list(filter(is_under_30, employees))
print(f"Employees under 30: {young_employees}")

# Example: Filtering out valid email addresses from a list

import re

emails = ["alice@example.com", "bob@", "charlie@domain.com", "diana@@example.com"]

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

valid_emails = list(filter(is_valid_email, emails))
print(f"Valid emails: {valid_emails}")