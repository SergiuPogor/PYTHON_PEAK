# Fibonacci sequence generator with Python's generator function
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a  # Yield current number in sequence
        a, b = b, a + b  # Move to next pair in the sequence

# Example usage in an application that needs real-time Fibonacci values
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

# Alternative: Generate Fibonacci numbers until a specific value
for fib in fibonacci_generator():
    if fib > 100:  # Stop after surpassing a certain value
        break
    print(f"Next Fibonacci: {fib}")

# Using generator expression to sum Fibonacci numbers below 1000
sum_fib_below_1000 = sum(f for f in fibonacci_generator() if f < 1000)
print(f"Sum of Fibonacci numbers below 1000: {sum_fib_below_1000}")