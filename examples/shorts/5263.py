class CustomIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Create an instance of CustomIterator
iterator = CustomIterator(1, 5)

# Using next() with a default value to handle StopIteration
for _ in range(7):
    print(next(iterator, "End of iterator"))