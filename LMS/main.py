import sys


class Library:
    """Class Library would LIST, LEND, RETURN or ADD book(s) to the library as per the input by the user"""

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("The books available in the library are : ")
        print("-------------->")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print(f"Great! {requestedBook} is available for you to borrow!!")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book you requested isn't currently available in the library")

    def returnBook(self, returnedBook):
        print("Thanks for returning the book!")
        self.availableBooks.append(returnedBook)


def main():
    listOfBooks = ["Harry Potter", "The Secret", "Power of the Subconscious Mind"]
    library = Library(listOfBooks)
    while True:
        print("""------ LIBRARY MENU ------
        1. Display all available books
        2. Request a book
        3. Return a book
        4. Exit
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
            sys.exit()


if __name__ == '__main__':
    main()

