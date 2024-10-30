class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
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
    custom_range = CustomRange(1, 10)

    for number in custom_range:
        print(number)
    
    # This will print numbers from 1 to 9