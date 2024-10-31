def generate_numbers(limit):
    for num in range(limit):
        yield num

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

def main():
    limit = 10
    
    # Chain generators
    numbers = generate_numbers(limit)
    even_numbers = filter_even(numbers)
    squared_numbers = square_numbers(even_numbers)

    # Print the squared even numbers
    for result in squared_numbers:
        print(result)

if __name__ == "__main__":
    main()