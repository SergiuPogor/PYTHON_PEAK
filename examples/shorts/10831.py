from functools import partial

# A function that calculates the total cost with tax
def calculate_total_cost(price, tax_rate, discount=0):
    return price + (price * tax_rate) - discount

# Using functools.partial to create a new function with a fixed tax rate
calculate_with_tax = partial(calculate_total_cost, tax_rate=0.07)

# Now you can call the new function with just price and discount
total1 = calculate_with_tax(100, discount=5)  # 100 + (100 * 0.07) - 5
total2 = calculate_with_tax(200)               # 200 + (200 * 0.07) - 0

# Demonstrating how it works with different prices
print(f'Total with tax (discount $5): ${total1:.2f}')  # Output: $102.00
print(f'Total with tax (no discount): ${total2:.2f}')  # Output: $214.00

# Another use case: partial for callback functions
def handle_event(event_type, message, user="Guest"):
    print(f'[{user}] {event_type}: {message}')

# Creating a specialized handler for error events
error_handler = partial(handle_event, event_type="ERROR")

# Using the error handler in different scenarios
error_handler("File not found")                     # Output: [Guest] ERROR: File not found
error_handler("Invalid input", user="Admin")       # Output: [Admin] ERROR: Invalid input