import sys


class Library:
    """Class Library would LIST, LEND, RETURN or ADD book(s) to the library as per the input by the user"""

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
        self.backup = listOfBooks
        self.borrowed_books = []

    def displayAvailableBooks(self):
        print("The books available in the library are : ")
        print("-------------->")
        for book in self.availableBooks:
            if book["quantity"] > 0:
                print(f'{book["name"]} by {book["author"]}')

    def lendBook(self, requestedBook):
        for book in self.availableBooks:
            if book["name"] == requestedBook:
                if book["quantity"] > 0:
                    book["quantity"] -= 1
                    if self.borrowed_books:
                        for backup_book in self.borrowed_books:
                            if backup_book["name"] == requestedBook:
                                backup_book["quantity_borrowed"] += 1
                    else:
                        self.borrowed_books.append(
                            {"name": requestedBook,
                             "quantity_borrowed": 1}
                        )
                    print(f"Great choice! {requestedBook} is now yours. Kindly return it within next 2 weeks!!")
                    return
        else:
            print("Sorry, the book you requested isn't currently available in the library")

    def addBook(self, newBook, qty):
        author = input("Please enter the author of the book: ")
        book = {
            "name": newBook,
            "author": author,
            "quantity": qty
                }
        self.availableBooks.append(book)
        self.backup.append(book)
        print("Thanks for the new addition to our Library!")

    def returnBook(self, returnedBook):
        qty = int(input("How many copies would you like to return? "))
        check = False
        if self.borrowed_books:
            for book in self.borrowed_books:
                if book["name"] == returnedBook:
                    if book["quantity_borrowed"] == 1 and qty == 1:
                        del self.borrowed_books[book]
                    else:
                        book["quantity_borrowed"] -= qty
                    for b in self.availableBooks:
                        if b["name"] == returnedBook:
                            b["quantity"] += qty
                            print("Thanks for returning the book(s)!")
                            check = True
        if not check:
            print("""Sorry! It seems like this book doesn't belong to this library 
                     but we would be honoured by this addition."
                     Would you like to donate it to our library?")
                     Enter 'Y' to continue or 'N' to return to the main menu""")
            answer = input()
            if answer == 'Y':
                self.addBook(returnedBook, qty)
            else:
                return


def main():
    listOfBooks = [
        {"name": "Harry Potter",
         "author": "J.K.Rowling",
         "quantity": 2},
        {"name": "The Secret",
         "author": "Rhonda Byrne",
         "quantity": 2},
        {"name": "The Power of your Subconscious Mind",
         "author": "Joseph Murphy",
         "quantity": 2}
    ]
    library = Library(listOfBooks)
    while True:
        print("""------ LIBRARY MENU ------
        1. Display all available books
        2. Request a book
        3. Return a book
        4. Add a book
        5. Exit
        """)
        choice = int(input("Enter Choice : "))
        if choice == 1:
            library.displayAvailableBooks()
        elif choice == 2:
            book = input("Enter the book you would like to borrow : ")
            library.lendBook(book)
        elif choice == 3:
            book = input("Enter the book you would like to return : ")
            library.returnBook(book)
        elif choice == 4:
            book = input("Enter the book you would like to add : ")
            library.addBook(book, 1)
        elif choice == 5:
            sys.exit()


if __name__ == '__main__':
    main()
