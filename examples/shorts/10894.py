from functools import lru_cache

# Simulating a slow function to calculate Fibonacci numbers
@lru_cache(maxsize=128)  # Caching the results to save time
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the performance
if __name__ == "__main__":
    import time

    start_time = time.time()
    print(f"Fibonacci of 35: {fibonacci(35)}")
    print(f"Execution time: {time.time() - start_time:.4f} seconds")

    # Repeated call to demonstrate the speed improvement
    start_time = time.time()
    print(f"Fibonacci of 35: {fibonacci(35)}")
    print(f"Execution time: {time.time() - start_time:.4f} seconds")