import requests

# Create a session object
session = requests.Session()

# Set a custom user agent for all requests
session.headers.update({'User-Agent': 'MyApp/1.0'})

# Function to get data from an API endpoint
def fetch_data(endpoint):
    response = session.get(endpoint)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# List of API endpoints to fetch data from
endpoints = [
    'https://api.example.com/data1',
    'https://api.example.com/data2',
    'https://api.example.com/data3'
]

# Fetching data from all endpoints using the session
results = []
for endpoint in endpoints:
    data = fetch_data(endpoint)
    results.append(data)

# Printing the fetched data
for result in results:
    print(result)

# Close the session when done
session.close()