import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_session():
    """Create a requests session with retry logic."""
    session = requests.Session()
    # Define the retry strategy
    retry_strategy = Retry(
        total=3,  # Total number of retries
        status_forcelist=[500, 502, 503, 504],  # HTTP status codes to retry
        method_whitelist=["HEAD", "GET", "OPTIONS"],  # Methods to retry
        backoff_factor=1  # Wait time between retries
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def fetch_data(url):
    """Fetch data from the given URL with retries."""
    session = create_session()  # Create a session with retry strategy
    try:
        response = session.get(url)  # Make a GET request
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data if successful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")  # Handle any request errors

if __name__ == "__main__":
    url = "https://api.example.com/data"  # Example API endpoint
    data = fetch_data(url)  # Fetch data with retries
    if data:
        print(data)  # Print the fetched data