def in_memory_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]  # Return cached result
        result = func(*args)  # Calculate and cache result
        cache[args] = result
        return result

    return wrapper

@in_memory_cache
def fetch_data(key):
    # Simulating a costly data fetching operation
    print(f"Fetching data for {key}...")
    return f"Data for {key}"

# Example usage
if __name__ == "__main__":
    print(fetch_data("user1"))  # Fetching data for user1
    print(fetch_data("user1"))  # Returns cached result
    print(fetch_data("user2"))  # Fetching data for user2
    print(fetch_data("user2"))  # Returns cached result