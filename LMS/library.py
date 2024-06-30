from book import Book
from customer import Customer


class Library:
    """Class Library would LIST, LEND, RETURN or ADD book(s) to the library as per the input by the user"""

    def __init__(self, listOfBooks: list[Book], listOfCustomers: list[Customer]):
        self.availableBooks = listOfBooks
        self.customers = listOfCustomers
        self.borrowed_books = []

    def get_customer(self, id: int):
        for cust in self.customers:
            if cust.id == id:
                return cust

    def displayAvailableBooks(self):
        for book in self.availableBooks:
            if self.is_book_available(book):
                print(f'Book: {book.name}')
                print(f'Author: {book.author}')
                print(f'Number of copies available : {book.quantity}')
                print(f'Volume: {book.volume}')
                print("--------------")

    # def lendBook(self, requestedBook):
    #     """lend_book(self, req_book:Book, customer: Customer)"""
    #     for book in self.availableBooks:
    #         if book.name == requestedBook:
    #             if self.is_book_available(book):
    #                 book.quantity -= 1
    #                 if self.borrowed_books:
    #                     for backup_book in self.borrowed_books:
    #                         if backup_book["name"] == requestedBook:
    #                             backup_book["quantity_borrowed"] += 1
    #                 else:
    #                     self.borrowed_books.append(
    #                         {"name": requestedBook,
    #                          "quantity_borrowed": 1}
    #                     )
    #                 print(f"Great choice! {requestedBook} is now yours. Kindly return it within next 2 weeks!!")
    #                 return
    #     else:
    #         print("Sorry, the book you requested isn't currently available in the library")

    def issue_book(self, requested_book: Book, current_customer: Customer):
        """Remove thr book from library catalog and then Add it to customer bag"""
        self.extract_from_catalog(requested_book)
        current_customer.add_book(requested_book)
        print(f"Great choice! {requested_book.name} is now yours. Kindly return it within next 2 weeks!!")

    def extract_from_catalog(self, book: Book):
        book.quantity -= 1

    def insert_to_catalog(self, book: Book):
        book.quantity += 1

    def addBook(self, newBook, qty):
        author = input("Please enter the author of the book: ")
        vol = input("Please enter the volume of the book: ")
        self.availableBooks.append(Book(newBook, author, qty, vol))
        print("Thanks for the new addition to our Library!")

    # def returnBook(self, returnedBook):
    #     qty = int(input("How many copies would you like to return? "))
    #     check = False
    #     if self.borrowed_books:
    #         for borrowed_book in self.borrowed_books:
    #             if borrowed_book["name"] == returnedBook:
    #                 if borrowed_book["quantity_borrowed"] == qty:
    #                     self.borrowed_books.remove(borrowed_book)
    #                 else:
    #                     borrowed_book["quantity_borrowed"] -= qty
    #                 for b in self.availableBooks:
    #                     if b.name == returnedBook:
    #                         b.quantity += qty
    #                         print("Thanks for returning the book(s)!")
    #                         check = True
    #     if not check:
    #         print("""Sorry! It seems like this book doesn't belong to this library but we would be honoured by this
    #         addition. Would you like to donate it to our library? Enter 'Y' to continue or 'N' to return to the main
    #         menu""")
    #         answer = input()
    #         if answer == 'Y':
    #             self.addBook(returnedBook, qty)
    #         else:
    #             return

    def return_book(self, returned_book: str, auth: str, vol: int, current_customer: Customer):
        book: Book = current_customer.search_book(returned_book, auth, vol)
        if book:
            current_customer.remove_book(book)
            self.insert_to_catalog(book)
            print("Thanks for returning the book!")
        else:
            print("It doesn't seem that the book was borrowed from this library. Please try again!")

    def number_of_books_available(self, book) -> int:
        for book1 in self.availableBooks:
            if book1.book_equal_to(book):
                return book1.quantity
        return 0

    def volumes_of_book_available(self, book):
        volumes = []
        for book1 in self.availableBooks:
            if book1.name == book:
                volumes.append(book1.volume)
        print(*volumes, sep=', ')

    def is_book_available(self, book):
        return 0 < book.quantity

    def search_by_word_in_book_name(self, word):
        books_with_word: list[Book] = []
        for book in self.availableBooks:
            if book.has_word(word):
                books_with_word.append(book)
        if books_with_word:
            print(f'All books available with the word "{word}" in their names are as follows: ')
            print(*books_with_word, sep='\n')
        else:
            print("Sorry, We are unable to locate any book having the word: ", word)

    def search_book(self, book_name: str, author: str) -> list[Book]:
        alike_books: list[Book] = []
        for book in self.availableBooks:
            if book.book_alike(book_name, author) and self.is_book_available(book):
                alike_books.append(book)
        return alike_books

    def print_books(self, books: list[Book]):
        for i, book in enumerate(books):
            print(f'{i + 1}. {book.name} by {book.author} - Volume {book.volume} . Copies available: {book.quantity}')
