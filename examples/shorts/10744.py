from functools import lru_cache

# A simple recursive function to calculate Fibonacci numbers
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = 35  # Large input to demonstrate speedup
    print("Fibonacci of", n, "is:", fibonacci(n))

if __name__ == "__main__":
    main()  # Execute the main function