class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Usage example
if __name__ == "__main__":
    custom_range = CustomRange(1, 5)
    for number in custom_range:
        print(number)