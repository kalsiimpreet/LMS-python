"""File that deals with all operations related to a specific book"""


class Book:

    def __init__(self, book, author, copies, vol):
        self.name: str = book
        self.author: str = author
        self.quantity: int = copies
        self.volume: int = vol

    def book_equal_to(self, other) -> bool:
        return self.name == other.name and self.author == other.author

    def book_name_equal_to(self, other) -> bool:
        return self.name == other.name

    def book_author_equal_to(self, other) -> bool:
        return self.author == other.author

    def has_word(self, word) -> bool:
        return word in self.name

    def book_alike(self, book_name: str, author_name: str):
        return book_name.lower() in self.name.lower() and author_name.lower() in self.author.lower()
