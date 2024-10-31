from functools import partial

# Let's say we have an API request function that accepts multiple parameters
def fetch_data(api_endpoint, query, max_retries=3, timeout=10):
    # Simulating data fetch with print statement
    print(f"Fetching from {api_endpoint} with query '{query}', retries: {max_retries}, timeout: {timeout}")
    # In real application, this would be an API request using requests.get or similar
    return {"status": "success", "data": "Sample data"}

# Using partial to lock in parameters for common API endpoints
fetch_users = partial(fetch_data, api_endpoint="https://api.example.com/users", max_retries=5)
fetch_posts = partial(fetch_data, api_endpoint="https://api.example.com/posts", timeout=15)

# Now, fetch_users and fetch_posts are like specialized versions of fetch_data
fetch_users(query="user_id=123")        # Output: Fetching from https://api.example.com/users with query 'user_id=123', retries: 5, timeout: 10
fetch_posts(query="post_id=789")        # Output: Fetching from https://api.example.com/posts with query 'post_id=789', retries: 3, timeout: 15

# Another example: Data processing where specific settings are fixed
def process_data(data, multiplier=1, offset=0):
    result = [(value * multiplier) + offset for value in data]
    print(f"Processed data with multiplier={multiplier}, offset={offset}: {result}")
    return result

# Fixing specific behavior for data scaling
scale_data = partial(process_data, multiplier=10)
offset_data = partial(process_data, offset=5)

# Using partial functions to apply specific transformations
scale_data([1, 2, 3])                  # Output: Processed data with multiplier=10, offset=0: [10, 20, 30]
offset_data([1, 2, 3])                 # Output: Processed data with multiplier=1, offset=5: [6, 7, 8]