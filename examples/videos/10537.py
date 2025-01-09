def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a  # Yield the current number
        a, b = b, a + b  # Update to the next Fibonacci numbers

# Using the generator to print Fibonacci numbers
fib_gen = fibonacci_generator()

# Display the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))

# Real-world application: Generating Fibonacci numbers on demand
def fibonacci_up_to_n(n):
    fib_gen = fibonacci_generator()
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(next(fib_gen))
    return fib_sequence

# Get Fibonacci numbers up to the 15th number
fib_numbers = fibonacci_up_to_n(15)
print("Fibonacci sequence up to 15:", fib_numbers)

# Using the Fibonacci generator in an application
def sum_fibonacci(n):
    return sum(fibonacci_up_to_n(n))

# Calculate the sum of the first 20 Fibonacci numbers
total_sum = sum_fibonacci(20)
print("Sum of first 20 Fibonacci numbers:", total_sum)