from functools import lru_cache

# Recursive function example: Fibonacci with lru_cache
@lru_cache(maxsize=128)  # Memoize results to speed up repeated calls
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Calculating large Fibonacci numbers efficiently
print("Fibonacci of 30:", fibonacci(30))  # Much faster with caching
print("Fibonacci of 35:", fibonacci(35))  # Uses stored results for efficiency
print("Fibonacci of 40:", fibonacci(40))  # Cached results make it nearly instant

# Example 2: Recursive function without lru_cache for comparison
def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

# Measuring speed difference with and without lru_cache
import time

start_time = time.time()
print("Fibonacci of 30 (slow):", slow_fibonacci(30))
print("Time without cache:", time.time() - start_time, "seconds")

start_time = time.time()
print("Fibonacci of 30 (fast):", fibonacci(30))
print("Time with lru_cache:", time.time() - start_time, "seconds")

# Practical use-case: Avoiding slowdowns in recursive calculations by adding caching
# lru_cache can transform functions that would be computationally expensive without memoization