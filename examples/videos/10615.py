class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

def main():
    custom_range = CustomRange(1, 10)

    print("Custom Range:")
    for number in custom_range:
        print(number)

    # Demonstrating the iterator state
    print("Iterating again:")
    for number in custom_range:  # This will not print anything
        print(number)

if __name__ == "__main__":
    main()