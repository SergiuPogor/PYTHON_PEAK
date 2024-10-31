# Standard string with embedded variables, calculations, and function calls using f-strings

import datetime
import os

# Example variables
user_name = "Alex"
balance = 1523.57
login_count = 5

# Example function for greeting
def personalized_greeting(name):
    return f"Welcome back, {name}!"

# Using f-strings for dynamic message creation
message = (
    f"Hello {user_name}, your current balance is ${balance:.2f}. "
    f"You've logged in {login_count} times this month. "
    f"{personalized_greeting(user_name)} Today is {datetime.datetime.now():%A, %B %d, %Y}."
)

print(message)

# Example with file paths and environment variables
file_path = "/tmp/test/output.txt"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
file_status = f"File '{file_path}' exists: {os.path.exists(file_path)}"
print(file_status)

# Example of f-strings with in-line calculations
discount = 0.1  # 10% discount
price = 99.99
discounted_price_message = f"The discounted price is ${price * (1 - discount):.2f}."
print(discounted_price_message)

# Advanced use: Combining variables, functions, and calculations
age = 28
years_until_retirement = lambda age: 65 - age
retirement_message = (
    f"User {user_name} is {age} years old and has "
    f"{years_until_retirement(age)} years until retirement."
)
print(retirement_message)