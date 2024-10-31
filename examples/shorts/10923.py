# Using functools.partial to simplify function calls
from functools import partial

# Function that calculates the total price after tax
def calculate_price(base_price, tax_rate, discount=0):
    total = base_price + (base_price * tax_rate) - discount
    return total

# Create a partial function with a fixed tax rate
calculate_price_with_tax = partial(calculate_price, tax_rate=0.2)

# Calculate price without discount
price1 = calculate_price_with_tax(100)
print(f"Total price with tax: {price1}")

# Create another partial function with tax rate and a fixed discount
calculate_discounted_price = partial(calculate_price, tax_rate=0.2, discount=10)

# Calculate price with discount
price2 = calculate_discounted_price(100)
print(f"Total price with tax and discount: {price2}")

# Using partial for a callback function
def print_price(price_calculator, base_price):
    total = price_calculator(base_price)
    print(f"The calculated price is: {total}")

# Use partial to create a callback with fixed base price
callback_with_fixed_base = partial(print_price, calculate_price_with_tax, base_price=200)
callback_with_fixed_base()