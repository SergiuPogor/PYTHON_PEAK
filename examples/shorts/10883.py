import requests

def fetch_data(url, session):
    response = session.get(url)
    return response.json()  # Assuming the API returns JSON data

def main():
    api_url = "https://api.example.com/data"  # Replace with your API URL

    with requests.Session() as session:
        # Set a default header for all requests
        session.headers.update({"Authorization": "Bearer your_token"})
        
        # Make multiple API calls
        for _ in range(5):
            data = fetch_data(api_url, session)
            print(data)  # Process your data here

if __name__ == "__main__":
    main()