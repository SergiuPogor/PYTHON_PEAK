from functools import lru_cache

# Calculating Fibonacci numbers without caching (slow for large n)
def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

# Fibonacci with caching using lru_cache, significantly faster
@lru_cache(maxsize=None)  # Cache unlimited results
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# Test both functions
print("Without Cache:", fibonacci_no_cache(30))  # Noticeable delay on large n
print("With Cache:", fibonacci_cached(30))  # Much faster

# Caching for recursive file search (simulate complex file directory parsing)
import os

@lru_cache(maxsize=100)
def search_files_with_cache(directory, target_extension=".txt"):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(target_extension):
                results.append(os.path.join(root, file))
    return results

# Assume a test directory with many subfolders and files
test_dir = "/tmp/test"
txt_files = search_files_with_cache(test_dir)
print("Text files found:", txt_files)

# Another recursive example - factorial
@lru_cache(maxsize=10)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Calculating large factorials without re-computation
print("Factorial of 10:", factorial(10))
print("Factorial of 15 (no re-compute for first 10):", factorial(15))