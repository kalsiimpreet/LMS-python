"""File that deals with all operations related to a specific book"""


class Book:

    def __init__(self, book, author, copies, vol):
        self.name = book
        self.author = author
        self.quantity = copies
        self.volume = vol

    def book_equal_to(self, other) -> bool:
        return self.name == other.name and self.author == other.author

    def book_name_equal_to(self, other) -> bool:
        return self.name == other.name

    def book_author_equal_to(self, other) -> bool:
        return self.author == other.author

    def has_word(self, word) -> bool:
        return word in self.name
