# This script demonstrates how to use functools.lru_cache
# to improve the performance of recursive Fibonacci calculation.

from functools import lru_cache

@lru_cache(maxsize=None)  # Cache unlimited number of results
def fibonacci(n):
    if n < 2:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

def main():
    num = 35  # Calculate Fibonacci of 35
    print(f"The {num}th Fibonacci number is: {fibonacci(num)}")

if __name__ == "__main__":
    main()