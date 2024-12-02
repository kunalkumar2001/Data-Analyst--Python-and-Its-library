class Library:

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_books(self):
        print("List of books:")
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def get_no_of_books(self):
        return self.no_of_books


# Creating a library object
library = Library()

# Adding books to the library
library.add_book("Book 1")
library.add_book("Book 2")
library.add_book("Book 3")

# Printing all books in the library
library.print_books()

# Getting the number of books in the library
num_books = library.get_no_of_books()
print("Number of books in the library:", num_books)
