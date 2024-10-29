# This script demonstrates the use of the enumerate function in Python,
# showing various use cases including basic list iteration,
# handling complex data structures, and custom starting indices.

def main():
    # Sample data for demonstration
    fruits = ["apple", "banana", "cherry", "date"]
    
    # Using enumerate to track index and value
    print("Basic usage of enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    
    # Starting enumeration from a custom index
    print("\nUsing a custom starting index:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}: {fruit}")
    
    # Working with a complex data structure (list of dictionaries)
    fruits_info = [
        {"name": "apple", "color": "red"},
        {"name": "banana", "color": "yellow"},
        {"name": "cherry", "color": "red"},
        {"name": "date", "color": "brown"}
    ]
    
    print("\nEnumerating through a list of dictionaries:")
    for index, fruit in enumerate(fruits_info):
        print(f"{index}: {fruit['name']} - {fruit['color']}")

    # Demonstrating error handling in case of complex data
    print("\nEnumerate with error handling:")
    try:
        for index, fruit in enumerate(fruits_info):
            if not isinstance(fruit, dict):
                raise ValueError("Expected a dictionary.")
            print(f"{index}: {fruit['name']} - {fruit['color']}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()