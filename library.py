# library.py

class Library:
	def __init__(self):
		self.books = []

	def add_book(self, book):
		self.books.append(book)

	def display_books(self):
		if not self.books:
			print("No books in the library.")
		else:
			print("Books in the library:")
			for book in self.books:
				book.display_info()
