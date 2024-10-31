from typing import List, Dict, Any

def process_data(data: List[Dict[str, Any]]) -> None:
    """
    Process a list of dictionaries containing user data.
    
    :param data: List of dictionaries with user information
    """
    for user in data:
        print(f"Processing user: {user['name']} (ID: {user['id']})")
        # Example logic could go here
        # Process other fields as needed

def main():
    user_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    process_data(user_data)

if __name__ == "__main__":
    main()