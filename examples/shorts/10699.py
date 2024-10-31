from functools import cache
import time

# Simulating an expensive computation
@cache
def slow_function(n):
    time.sleep(2)  # Simulate a delay
    return n * n

# Testing the caching mechanism
def main():
    print("Calculating...") 
    print(slow_function(4))  # Takes 2 seconds
    print(slow_function(4))  # Instant return due to cache
    print(slow_function(5))  # Takes 2 seconds
    print(slow_function(5))  # Instant return due to cache

if __name__ == "__main__":
    main()