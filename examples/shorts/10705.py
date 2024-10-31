# Example of using generator expressions to handle large datasets

def get_square_numbers(n):
    # This is a generator expression that yields square numbers
    return (i * i for i in range(n))

def main():
    n = 1000000  # Large number for demonstration
    squares = get_square_numbers(n)

    # Process the squares without using too much memory
    for square in squares:
        if square > 100:  # Filtering condition
            print(square)

if __name__ == "__main__":
    main()