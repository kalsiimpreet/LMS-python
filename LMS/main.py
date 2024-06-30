"""LIBRARY MANAGEMENT SYSTEM"""
import sys

from book import Book
from library import Library


def main():
    listOfBooks = [
        Book("Harry Potter", "J.K.Rowling", 2, 1),
        Book("Harry Potter", "J.K.Rowling", 2, 2),
        Book("Harry Potter", "J.K.Rowling", 2, 3),
        Book("The Secret", "Rhonda Byrne", 2, 1),
        Book("The Power of your Subconscious Mind", "Joseph Murphy", 2, 1)
    ]
    library = Library(listOfBooks)
    while True:
        print("""------ LIBRARY MENU ------
        1. Display all available books
        2. Request a book
        3. Return a book
        4. Add a book
        5. Find all books containing the word you provide
        6. Display all Volumes of the book
        7. Exit
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
            qty = int(input("How many copies would you like to donate? "))
            library.addBook(book, qty)
        elif choice == 5:
            word = input("Enter the word you would like to search for : ")
            library.search_by_word_in_book_name(word)
        elif choice == 6:
            book = input("Enter the book you would like to see the volumes for : ")
            library.volumes_of_book_available(book)
        elif choice == 7:
            sys.exit()


if __name__ == '__main__':
    main()
