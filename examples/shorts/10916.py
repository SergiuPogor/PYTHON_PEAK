# Using requests.Session to Optimize Multiple API Requests

import requests

def fetch_data_with_session(api_url, endpoints):
    # Initialize a session to maintain headers and connection settings
    with requests.Session() as session:
        session.headers.update({"User-Agent": "DataFetcherBot/1.0"})  # Set common headers

        responses = []
        for endpoint in endpoints:
            # Use the same session for multiple requests, improving performance
            response = session.get(f"{api_url}/{endpoint}")
            if response.status_code == 200:
                responses.append(response.json())
            else:
                responses.append({"error": response.status_code, "endpoint": endpoint})
        
        return responses

# Usage example
api_base_url = "https://api.example.com/v1"
endpoints_to_fetch = ["user/123", "data/stats", "posts/latest", "comments/recent"]
api_responses = fetch_data_with_session(api_base_url, endpoints_to_fetch)
print(api_responses)