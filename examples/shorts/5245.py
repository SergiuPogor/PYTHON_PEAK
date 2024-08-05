# Using divmod to handle complex calculations

# Example 1: Financial Calculation
total_cents = 2578
dollars, cents = divmod(total_cents, 100)
print(f"Total: {dollars} dollars and {cents} cents")

# Example 2: Pagination
total_items = 125
items_per_page = 10
pages, remaining_items = divmod(total_items, items_per_page)
print(f"Pages needed: {pages}, Items on last page: {remaining_items}")

# Example 3: Time Conversion
total_seconds = 7384
minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f"Time: {hours} hours, {minutes} minutes, and {seconds} seconds")

# Example 4: Complex Mathematical Operation
a, b = 27, 4
quotient, remainder = divmod(a, b)
print(f"{a} divided by {b} is {quotient} with a remainder of {remainder}")

# Example 5: Large Number Division
large_number = 123456789
divisor = 123
quotient, remainder = divmod(large_number, divisor)
print(f"{large_number} divided by {divisor} is {quotient} with a remainder of {remainder}")
