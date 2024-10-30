import time

# Decorator to cache function results
def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        print(f"Calculating result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# Simulated heavy computation function
@cache_results
def factorial(n):
    time.sleep(2)  # Simulate a delay for computation
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the caching decorator
print("Factorial of 5:", factorial(5))  # Should calculate and cache
print("Factorial of 5 again:", factorial(5))  # Should use cached result

print("Factorial of 6:", factorial(6))  # Should calculate and cache
print("Factorial of 6 again:", factorial(6))  # Should use cached result

print("Factorial of 5 again:", factorial(5))  # Should use cached result again