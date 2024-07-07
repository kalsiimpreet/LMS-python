"""LIBRARY MANAGEMENT SYSTEM"""
import sys

from catalog import Catalog
from book import Book
from customer import Customer
from library import Library


def request_book_flow(library: Library, cust: Customer):
    book_name: str = input("Enter the book or a keyword that you would like to borrow : ")
    author: str = input("Enter the author : ")
    alike_books: list[Catalog] = library.search_catalog(book_name, author)
    print("Following book(s) seem to match your search. Kindly choose the required book by its serial number :")
    library.print_books(alike_books)
    sr_no_of_chosen_book: int = int(input())
    if sr_no_of_chosen_book > len(alike_books) or sr_no_of_chosen_book < 0:
        print("Seems like you chose a wrong option. Enter 'Y' to continue or 'N' to exit: ")
        option = input()
        if option.upper() == 'Y':
            request_book_flow(library, cust)
        else:
            return
    chosen_book: Catalog = alike_books[sr_no_of_chosen_book - 1]
    library.issue_book(chosen_book, cust)


def return_book_flow(library: Library, cust: Customer):
    book = input("Enter the book you would like to return : ")
    author = input("Enter the author : ")
    vol = int(input("Enter Volume of book : "))
    library.return_book(book, author, vol, cust)


def main():
    list_of_books_in_catalog = [
        Catalog("Harry Potter", "J.K.Rowling", 1, 1),
        Catalog("Harry Potter", "J.K.Rowling", 2, 2),
        Catalog("Harry Potter", "J.K.Rowling", 3, 2),
        Catalog("The Secret", "Rhonda Byrne", 1, 1),
        Catalog("The Power of your Subconscious Mind", "Joseph Murphy", 1, 1)
    ]

    list_of_customers = [
        Customer(1, "Akash"),
        Customer(2, "Rohit"),
        Customer(3, "Alisha"),
        Customer(4, "Anchal")
    ]

    library = Library(list_of_books_in_catalog, list_of_customers)
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
            7. Display customer bag
            8. Exit
            """)
            choice = int(input("Enter Choice : "))
            if choice == 1:
                library.displayAvailableBooks()
            elif choice == 2:
                request_book_flow(library, cust)
            elif choice == 3:
                return_book_flow(library, cust)
            elif choice == 4:
                book = input("Enter the book you would like to add : ")
                author = input("Enter the book author : ")
                vol = int(input("Enter Volume of the book  : "))
                copies = int(input("How many copies would you like to donate? "))
                library.add_new_book(book, author, vol, copies)
            elif choice == 5:
                word = input("Enter the word you would like to search for : ")
                library.search_by_word_in_book_name(word)
            elif choice == 6:
                book = input("Enter the book you would like to see the volumes for : ")
                author = input("Enter the book author : ")
                library.volumes_of_book_available(book, author)
            elif choice == 7:
                library.display_customer_bag(cust)
            elif choice == 8:
                sys.exit()
        else:
            print("Sorry, this customer ID is not registered with our library. Please try again.")


if __name__ == '__main__':
    main()
