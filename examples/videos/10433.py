from functools import reduce

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def main():
    # List of numbers for reduction
    numbers = [1, 2, 3, 4, 5]

    # Using reduce to multiply all numbers
    product = reduce(multiply, numbers)
    print(f"Product of numbers: {product}")

    # Using reduce to add all numbers
    sum_result = reduce(add, numbers)
    print(f"Sum of numbers: {sum_result}")

    # Using lambda with reduce to find maximum
    max_value = reduce(lambda x, y: x if x > y else y, numbers)
    print(f"Maximum value: {max_value}")

    # Using reduce to create a string from list
    words = ["Hello", "world", "from", "Python"]
    sentence = reduce(lambda x, y: f"{x} {y}", words)
    print(f"Sentence: {sentence.strip()}")

if __name__ == "__main__":
    main()