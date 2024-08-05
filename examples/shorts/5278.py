class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_info):
        # Create a Book instance from a string
        title, author = book_info.split(',')
        return cls(title, author)

    @classmethod
    def get_class_info(cls):
        # Method to return class information
        return f"This class represents a book with title and author."

def main():
    # Using classmethod to create an instance
    book_info = "1984,George Orwell"
    book = Book.from_string(book_info)
    
    # Print book details and class info
    print(f"Book title: {book.title}")
    print(f"Book author: {book.author}")
    print(Book.get_class_info())

if __name__ == "__main__":
    main()
