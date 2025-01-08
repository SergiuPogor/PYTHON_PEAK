from collections import namedtuple

# Define a namedtuple for storing book information
Book = namedtuple('Book', ['title', 'author', 'year', 'genre'])

def main():
    # Create a list of books using the namedtuple
    books = [
        Book(title='1984', author='George Orwell', year=1949, genre='Dystopian'),
        Book(title='To Kill a Mockingbird', author='Harper Lee', year=1960, genre='Fiction'),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', year=1925, genre='Classic'),
    ]

    # Print book information
    for book in books:
        print(f"{book.title} by {book.author} ({book.year}) - Genre: {book.genre}")

    # Accessing specific book information by name
    first_book = books[0]
    print(f"First Book: {first_book.title}, Author: {first_book.author}")

    # Unpacking namedtuples
    title, author, year, genre = first_book
    print(f"Unpacked - Title: {title}, Author: {author}, Year: {year}, Genre: {genre}")

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()