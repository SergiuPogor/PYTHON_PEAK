import itertools

# Function to demonstrate itertools.tee()
def demonstrate_tee():
    # Create an iterable of numbers
    numbers = range(1, 11)  # Numbers from 1 to 10
    # Clone the iterator
    it1, it2 = itertools.tee(numbers, 2)  # Create two independent iterators

    # Example of processing with the first iterator
    print("Processing first iterator:")
    for number in it1:
        if number % 2 == 0:  # Check for even numbers
            print(f"Even number: {number}")

    # Example of processing with the second iterator
    print("\nProcessing second iterator:")
    for number in it2:
        if number % 2 != 0:  # Check for odd numbers
            print(f"Odd number: {number}")

# Main function to run the example
def main():
    demonstrate_tee()

if __name__ == "__main__":
    main()

# This script demonstrates the use of itertools.tee() 
# to create two independent iterators from a single iterable 
# and processes them separately, showing even and odd numbers.