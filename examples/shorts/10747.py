from typing import Dict, Callable

class SimpleCache:
    """A simple in-memory cache implementation."""
    def __init__(self):
        self.cache: Dict[str, int] = {}

    def get(self, key: str) -> int:
        """Get value from cache if exists."""
        return self.cache.get(key)

    def set(self, key: str, value: int):
        """Set value in cache."""
        self.cache[key] = value

def expensive_function(x: int) -> int:
    """Simulates an expensive computation."""
    result = x * x  # Imagine this takes time
    return result

def cached_function(x: int, cache: SimpleCache) -> int:
    """Function that uses cache to avoid recomputation."""
    cached_result = cache.get(str(x))
    if cached_result is not None:
        return cached_result  # Return cached result

    result = expensive_function(x)
    cache.set(str(x), result)  # Cache the new result
    return result

def main():
    cache = SimpleCache()
    print("Result 1:", cached_function(5, cache))  # Computes and caches
    print("Result 2:", cached_function(5, cache))  # Returns cached result

if __name__ == "__main__":
    main()