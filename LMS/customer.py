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

    def get_book(self, check_book: str) -> Book:
        for book in self.bag:
            if book.name == check_book:
                return book

    def remove_book(self, book: Book):
        self.bag.remove(book)