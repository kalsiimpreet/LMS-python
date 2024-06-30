"""LIBRARY MANAGEMENT SYSTEM"""
import sys

from book import Book
from customer import Customer
from library import Library


def request_book_flow(library: Library, cust: Customer):
    book = input("Enter the book you would like to borrow : ")
    author = input("Enter the author : ")
    alike_books = library.search_book(book, author)
    print("Following book(s) seem to match your search. Kindly choose the required book by its serial number :")
    library.print_books(alike_books)
    sr_no_of_chosen_book: int = int(input())
    chosen_book: Book = alike_books[sr_no_of_chosen_book - 1]
    library.issue_book(chosen_book, cust)


def main():
    listOfBooks = [
        Book("Harry Potter", "J.K.Rowling", 2, 1),
        Book("Harry Potter", "J.K.Rowling", 2, 2),
        Book("Harry Potter", "J.K.Rowling", 2, 3),
        Book("The Secret", "Rhonda Byrne", 2, 1),
        Book("The Power of your Subconscious Mind", "Joseph Murphy", 2, 1)
    ]

    listOfCustomers = [
        Customer(1, "Akash"),
        Customer(2, "Rohit"),
        Customer(3, "Alisha"),
        Customer(4, "Anchal")
    ]

    library = Library(listOfBooks, listOfCustomers)
    while True:
        customer_id = int(input("Kindly enter your customer ID : "))
        cust = library.get_customer(customer_id)
        if cust:
            print("Welcome", cust.name, "! How can we help you today?")
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
                request_book_flow(library, cust)
            elif choice == 3:
                book = input("Enter the book you would like to return : ")
                library.return_book(book, cust)
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
        else:
            print("Sorry, this customer ID is not registered with our library. Please try again.")


if __name__ == '__main__':
    main()
