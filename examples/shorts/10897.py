from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    print("Fibonacci of 10:", fibonacci(10))  # Output: 55
    print("Fibonacci of 20:", fibonacci(20))  # Output: 6765
    print("Fibonacci of 30:", fibonacci(30))  # Output: 832040

    # Cache info
    print("Cache info:", fibonacci.cache_info())  # Check cache status