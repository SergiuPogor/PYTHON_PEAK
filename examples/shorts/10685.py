class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            current_value = self.current
            self.current += 1
            return current_value

# Example usage
def main():
    # Create a custom iterator from 1 to 5
    for number in CustomRange(1, 6):
        print(number)

# Run the main function to see the iterator in action
main()

# Another use case: Custom iterator for a list of strings
class StringReverser:
    def __init__(self, strings):
        self.strings = strings
        self.index = len(strings)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.strings[self.index][::-1]

# Example usage
def reverse_strings():
    words = ["hello", "world", "Python"]
    for reversed_word in StringReverser(words):
        print(reversed_word)

# Run the function to see the string reverser in action
reverse_strings()