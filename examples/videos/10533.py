name = "Alice"
age = 30
balance = 1234.56

# Using f-strings for dynamic string formatting
welcome_message = f"Hello, {name}! You are {age} years old."
account_info = f"Your account balance is ${balance:.2f}."

# More complex expressions
greeting = f"{name.upper()} has a balance of {balance * 2:.2f}."
summary = f"Welcome {name}, your balance doubled is ${balance * 2:.2f}."

# Display messages
print(welcome_message)
print(account_info)
print(greeting)
print(summary)

# Using f-strings in a loop for multiple users
users = [
    {"name": "Alice", "age": 30, "balance": 1234.56},
    {"name": "Bob", "age": 25, "balance": 987.65},
    {"name": "Charlie", "age": 35, "balance": 5000.00}
]

for user in users:
    user_message = f"User: {user['name']}, Age: {user['age']}, Balance: ${user['balance']:.2f}"
    print(user_message)