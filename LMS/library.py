from book import Book
from catalog import Catalog
from customer import Customer


class Library:
    """Class Library would LIST, LEND, RETURN or ADD book(s) to the library as per the input by the user"""

    def __init__(self, list_of_books: list[Catalog], list_of_customers: list[Customer]):
        self.available_books = list_of_books
        self.customers = list_of_customers
        self.borrowed_books = []

    def get_customer(self, cust_id: int):
        for cust in self.customers:
            if cust.id == cust_id:
                return cust

    def displayAvailableBooks(self):
        for book in self.available_books:
            if book.is_book_available():
                print(f'Book: {book.name}')
                print(f'Author: {book.author}')
                print(f'Volume: {book.volume}')
                print(f'Number of copies available : {len(book.copies)}')
                print("--------------")

    def issue_book(self, requested_book: Catalog, current_customer: Customer):
        """Remove thr book from library catalog and then Add it to customer bag"""
        book_to_issue = self.extract_from_catalog(requested_book)
        current_customer.add_book(book_to_issue)
        print(f"Great choice! {book_to_issue.name} by {book_to_issue.author}, Volume-{book_to_issue.volume} "
              f"is now yours. Kindly return it within next 2 weeks!!")

    def search_catalog(self, book_name: str, author: str) -> list[Catalog]:
        alike_books = []
        for book in self.available_books:
            if book.book_alike(book_name, author) and book.is_book_available():
                alike_books.append(book)
        return alike_books

    def extract_from_catalog(self, book: Catalog) -> Book:
        return book.remove_book()

    def insert_to_catalog(self, book_to_insert: Book):
        # book.quantity += 1
        for book in self.available_books:
            if book.book_alike(book_to_insert.name, book_to_insert.author):
                book.add_copy_of_book(book_to_insert.book_id)
                return

    def add_new_book(self, book_name: str, author: str, vol: int, copies: int):
        self.available_books.append(Catalog(book_name, author, vol, copies))
        print("Thanks for the new addition to our Library!")

    def return_book(self, returned_book: str, auth: str, vol: int, current_customer: Customer):
        book: Book = current_customer.search_book(returned_book, auth, vol)
        if book:
            current_customer.remove_book(book)
            self.insert_to_catalog(book)
            print("Thanks for returning the book!")
        else:
            print("It seems that the book was not borrowed from this library. "
                  "Would you like to donate this book to our library? Enter 'Y' to continue, 'N' to exit.")
            answer = input()
            if answer.lower() == "Y".lower():
                self.add_new_book(returned_book, auth, vol, 1)
            else:
                return

    def volumes_of_book_available(self, book_name: str, author: str):
        volumes = []
        for book1 in self.available_books:
            if book1.book_alike(book_name, author):
                volumes.append(book1.volume)
        print("Volume available are : ")
        print(*volumes, sep=', ')

    def search_by_word_in_book_name(self, word: str):
        books_with_word: list[Catalog] = []
        for book in self.available_books:
            if book.has_word(word):
                books_with_word.append(book)
        if books_with_word:
            print(f'All books available with the word "{word}" in their names are as follows: ')
            # print(*books_with_word, sep='\n')
            self.print_books(books_with_word)
        else:
            print("Sorry, We are unable to locate any book having the word: ", word)

    def print_books(self, books: list[Catalog]):
        if books:
            for i, book in enumerate(books):
                print(f'{i + 1}. {book.name} by {book.author} - Volume {book.volume} . Copies available: '
                      f'{len(book.copies)}')
        else:
            print("Sorry, there are no books to display.")

    def display_customer_bag(self, current_customer: Customer):
        if current_customer.id:
            self.print_customer_books(current_customer)

    def print_customer_books(self, cust: Customer):
        books = cust.bag
        if books:
            print(f'{cust.name} has the following book(s) in their bag :')
            for i, book in enumerate(books):
                print(f'{i + 1}. {book.name} by {book.author} - Volume {book.volume}')
        else:
            print("Sorry, there are no books to display.")
