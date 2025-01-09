from requests.exceptions import HTTPError, Timeout
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type, retry_if_result
import requests

# Define URL for the request
url = 'https://fake-json-api.mock.beeceptor.com/users'

# Retry settings: exponential backoff, retry up to 5 times
@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(5))
def fetch_data_with_retry():
    # Attempt to get the data from the API
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"Response Status Code: {response.status_code}")  # Debugging
        return response  # Return the response object for further processing
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise  # Raise error for retry mechanism
    except Timeout:
        print("Request timed out; retrying...")
        raise  # Raise error to trigger retry
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        raise  # Raise error for retry mechanism

try:
    response = fetch_data_with_retry()
    print("Response Status Code:", response.status_code)
    data = response.json()
    print("Data fetched successfully:", data)
except Exception as final_error:
    print("Failed to fetch data after multiple retries:", final_error)

# Alternative example with retry on specific status codes
@retry(
    wait=wait_exponential(multiplier=1, min=1, max=5),
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type(HTTPError) | retry_if_result(lambda x: x.status_code in {500, 502, 503}),
)
def fetch_retry_on_status():
    try:
        response = requests.get(url, timeout=5)

        # Ensure the response is valid
        print(f"Response Status Code: {response.status_code}")  # Debugging
        if response.status_code != 200:
            print(f"Received status code {response.status_code}, retrying...")
            raise HTTPError(f"Unexpected status code: {response.status_code}")

        return response  # Return the response object
    except HTTPError as http_err:
        print(f"HTTPError: {http_err}")
        raise
    except Exception as e:
        print(f"General Error: {e}")
        raise

try:
    response = fetch_retry_on_status()
    print("Response Status Code:", response.status_code)
    result = response.json()
    print("Data fetched with status-based retry:", result)
except Exception as e:
    print("Failed to retrieve data after retries:", e)



