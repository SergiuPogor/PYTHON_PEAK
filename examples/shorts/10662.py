import contextlib
import requests

# Function to fetch data from a URL safely
@contextlib.contextmanager
def fetch_url(url):
    response = requests.get(url)
    try:
        # Ensure that we close the response when done
        yield response
    finally:
        response.close()

# Example usage
if __name__ == "__main__":
    url = 'https://api.example.com/data'
    with fetch_url(url) as resp:
        # Use the response data
        data = resp.json()
        print(data)