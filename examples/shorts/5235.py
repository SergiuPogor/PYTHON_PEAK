# Example 1: Basic usage of all() function
numbers = [1, 2, 3, 4, 5]
all_positive = all(n > 0 for n in numbers)
print(all_positive)  # Output: True

# Example 2: Validating form inputs
form_data = {
    "username": "user123",
    "password": "pass1234",
    "email": "user@example.com"
}

is_valid = all(form_data.values())
print(is_valid)  # Output: True

# Example 3: Checking conditions in a list of dictionaries
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": True},
    {"name": "Charlie", "active": False}
]

all_active = all(user["active"] for user in users)
print(all_active)  # Output: False

# Example 4: Using all() with a nested iterable
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_elements_positive = all(all(n > 0 for n in sublist) for sublist in nested_list)
print(all_elements_positive)  # Output: True

# Example 5: Combining all() with any() for complex conditions
complex_conditions = [
    [True, False, True],
    [True, True, True],
    [False, False, True]
]

result = all(any(cond) for cond in complex_conditions)
print(result)  # Output: True