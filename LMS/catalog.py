from book import Book


class Catalog:

    def __init__(self, book_name: str, author: str, volume: int, copies: int):
        self.name = book_name
        self.author = author
        self.volume = volume
        self.copies = [Book(self.name, self.author, self.volume, i + 1) for i in range(copies)]

    def remove_book(self):
        return self.copies.pop()

    def add_copy_of_book(self, book_id: int):
        self.copies.append(Book(self.name, self.author, self.volume, book_id))

    def is_book_available(self):
        return 0 < len(self.copies)

    def has_word(self, word) -> bool:
        return word.lower() in self.name.lower()

    def book_alike(self, book_name: str, author_name: str):
        return book_name.lower() in self.name.lower() and author_name.lower() in self.author.lower()
