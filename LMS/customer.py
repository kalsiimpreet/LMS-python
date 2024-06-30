"""
Class to deal with customers
"""
from book import Book


class Customer:

    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name
        self.bag: list[Book] = []

    def add_book(self, book: Book):
        self.bag.append(book)

    def get_books(self, check_book: str) -> Book:
        for book in self.bag:
            if check_book in book.name:
                return book

    def search_book(self, book_name: str, author_name: str, vol: int):
        for book in self.bag:
            if (book_name.lower() in book.name.lower() and author_name.lower() in book.author.lower() and vol ==
                    book.volume):
                return book

    def remove_book(self, book: Book):
        self.bag.remove(book)
