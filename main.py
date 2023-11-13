# main.py

from book import Book
from library import Library

def main():
    # Create books
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0-06-112008-1")
    book3 = Book("1984", "George Orwell", "978-0-452-28423-4")

    # Create a library
    my_library = Library()

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Display books in the library
    my_library.display_books()

if __name__ == "__main__":
    main()

