from search import search_name, search_genre, search_year
from add import add_book
from delete import delete_book
from edit import edit_book


Books = {
    "book1": {
        "name": "Punisher Max: In the Beginning",
        "genre": "Crime",
        "year": 2004
    },
    "book2": {
        "name": "Captain America: The Winter Soldier",
        "genre": "Adventure",
        "year": 2005
    },
    "book3": {
        "name": "Black Widow: The Name of the Rose",
        "genre": "Action",
        "year": 2010
    }
}


def search_books(books):
    print("\n===== SEARCH BOOKS =====")
    print("1. Search by book name")
    print("2. Search by genre")
    print("3. Search by publication year")

    choice = input("How would you like to search? ")

    if choice == "1":
        search_name(books)
    elif choice == "2":
        search_genre(books)
    elif choice == "3":
        search_year(books)
    else:
        print("Invalid choice.")


def menu(books):
    while True:
        print("\n===== BOOK INVENTORY =====")
        print("1. Search")
        print("2. Add")
        print("3. Delete")
        print("4. Edit")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_books(books)

        elif choice == "2":
            add_book(books)

        elif choice == "3":
            delete_book(books)

        elif choice == "4":
            edit_book(books)

        elif choice == "5":
            print("\nThank you for using the Book Inventory System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


menu(Books)
