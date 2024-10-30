import itertools

def generate_numbers():
    """Generator that yields numbers from 1 to 5."""
    for i in range(1, 6):
        yield i

def generate_letters():
    """Generator that yields letters from A to E."""
    for letter in 'ABCDE':
        yield letter

def combine_iterators():
    """Combine numbers and letters using itertools.chain."""
    numbers = generate_numbers()
    letters = generate_letters()
    
    combined = itertools.chain(numbers, letters)
    return list(combined)

def process_data():
    """Main function to demonstrate chaining."""
    combined_data = combine_iterators()
    print("Combined data from iterators:")
    for item in combined_data:
        print(item)

if __name__ == "__main__":
    process_data()