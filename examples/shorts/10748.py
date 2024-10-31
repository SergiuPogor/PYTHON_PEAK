from typing import Final

# Define constants using typing.Final
MAX_CONNECTIONS: Final[int] = 10
API_URL: Final[str] = "https://api.example.com"

def connect_to_service():
    """Simulates connecting to a service with constants."""
    print(f"Connecting to {API_URL} with a maximum of {MAX_CONNECTIONS} connections.")

def change_constant_example():
    """Shows what happens if you try to change a constant."""
    try:
        # Uncommenting the following line will raise an error in type checkers
        # API_URL = "https://new-api.example.com"  # Attempt to change a constant
        print("Trying to change API_URL, but it's a constant!")
    except Exception as e:
        print("Error:", e)

def main():
    connect_to_service()
    change_constant_example()

if __name__ == "__main__":
    main()