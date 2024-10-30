import os

def get_database_url():
    # Use os.getenv to retrieve the database URL from environment variables
    database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    
    # Log the URL for debugging purposes
    print(f"Database URL: {database_url}")
    return database_url

def get_api_key():
    # Get the API key, defaulting to None if not set
    api_key = os.getenv('API_KEY')
    
    if api_key is None:
        print("Warning: API_KEY is not set.")
    return api_key

def main():
    # Retrieve configuration data
    db_url = get_database_url()
    api_key = get_api_key()
    
    # Simulate application logic using the retrieved configurations
    if api_key:
        print("Connecting to API with the provided key...")
        # Here you would add the logic to connect to your API
    else:
        print("Failed to connect: No API key provided.")

if __name__ == "__main__":
    main()

# This code demonstrates how to use os.getenv to safely retrieve
# environment variables in Python. It includes default values for
# better safety and handles potential errors gracefully.