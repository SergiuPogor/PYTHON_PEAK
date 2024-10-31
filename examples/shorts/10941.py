from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 10

# Example of floating-point issue
float_a = 0.1 + 0.2
float_b = 0.3

# Print floating-point comparison
print(f"Floating-point result: {float_a}, equals 0.3? {float_a == float_b}")

# Using Decimal for precise calculations
decimal_a = Decimal('0.1') + Decimal('0.2')
decimal_b = Decimal('0.3')

# Print Decimal comparison
print(f"Decimal result: {decimal_a}, equals 0.3? {decimal_a == decimal_b}")

# Another practical use case
prices = [Decimal('19.99'), Decimal('5.49'), Decimal('3.50')]
total_price = sum(prices)

# Print total price
print(f"Total Price: {total_price}")