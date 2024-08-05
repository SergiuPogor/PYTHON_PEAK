class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def main():
    # Create an instance of Person
    person = Person("Alice", 30)

    # Print using repr() for detailed debugging
    print(repr(person))

if __name__ == "__main__":
    main()
