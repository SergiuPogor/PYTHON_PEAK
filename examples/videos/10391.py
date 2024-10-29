# This script demonstrates how to use functools.lru_cache
# to optimize a recursive Fibonacci function.

from functools import lru_cache

@lru_cache(maxsize=None)  # Cache all results without limit
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Testing the optimized Fibonacci function
    test_values = [5, 10, 15, 20, 25, 30]
    
    for value in test_values:
        print(f"Fibonacci of {value} is {fibonacci(value)}")

if __name__ == "__main__":
    main()