# Pythonic trick: Using generators for memory-efficient data streaming and processing

# Example 1: Generator to process a large file line-by-line, without loading it all into memory
def stream_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Use generator to handle the data efficiently
for log_entry in stream_file('/tmp/test/input.txt'):
    print("Log Entry:", log_entry)

# Example 2: Creating an infinite sequence generator, useful for continuous data processing
def endless_count(start=1):
    while True:
        yield start
        start += 1

# Taking only the first 5 results from an infinite generator
counter = endless_count()
for _ in range(5):
    print("Counter:", next(counter))

# Example 3: Memory-efficient generator for Fibonacci series, a common real-life use case
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Fetching only the first 10 Fibonacci numbers
fib_gen = fibonacci()
for _ in range(10):
    print("Fibonacci:", next(fib_gen))

# Example 4: Using generator expressions for quick and memory-efficient data processing
numbers = (x * 2 for x in range(10**6) if x % 2 == 0)

# Summing first 10 even, doubled numbers generated on the fly
total = sum(next(numbers) for _ in range(10))
print("Sum of first 10 processed numbers:", total)