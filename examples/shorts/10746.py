from typing import List

def process_numbers(numbers: List[int]) -> int:
    """Calculates the sum of a list of integers."""
    total = sum(numbers)
    return total

def main():
    try:
        numbers = [1, 2, 3, 4, 5]  # This is a valid list of integers
        result = process_numbers(numbers)
        print("Sum of numbers:", result)

        # Example with invalid data type
        mixed_numbers = [1, '2', 3]  # This will cause a type error
        result = process_numbers(mixed_numbers)
    except TypeError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()  # Execute the main function