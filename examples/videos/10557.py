class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r})"

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

# Creating instances of Book
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

# Using __repr__ for debugging
print("Debugging with __repr__:")
print(repr(book1))
print(repr(book2))

# Using __str__ for user-friendly output
print("\nUser-friendly output with __str__:")
print(str(book1))
print(str(book2))

# Creating a list of books
library = [book1, book2]

# Debugging the library contents
print("\nDebugging library contents:")
for book in library:
    print(repr(book))

# Adding another book and checking again
library.append(Book("Brave New World", "Aldous Huxley", 1932))
print("\nUpdated library contents:")
for book in library:
    print(repr(book))