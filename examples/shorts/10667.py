from typing import List, Dict

# Function that accepts a list of numbers and returns their square
def square_numbers(numbers: List[int]) -> List[int]:
    return [n ** 2 for n in numbers]

# Function that takes user details and returns a dictionary
def create_user(username: str, age: int) -> Dict[str, str]:
    return {'username': username, 'age': str(age)}

# Example usage
if __name__ == "__main__":
    # Square numbers example
    numbers = [1, 2, 3, 4, 5]
    squared = square_numbers(numbers)
    print("Squared Numbers:", squared)

    # Create user example
    user = create_user("Alice", 30)
    print("User Details:", user)