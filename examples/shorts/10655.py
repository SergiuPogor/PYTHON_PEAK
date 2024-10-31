# Custom iterator example using __iter__ and __next__

class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End the iteration
        value = self.current
        self.current -= 1  # Decrement for the next call
        return value

# Example usage
countdown = Countdown(5)

for number in countdown:
    print(number)  # Outputs: 5, 4, 3, 2, 1, 0

# Creating another custom iterator with a list
class ListIterator:
    def __init__(self, data: list):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Example usage
my_list = ListIterator(['a', 'b', 'c', 'd'])
for item in my_list:
    print(item)  # Outputs: a, b, c, d