def search_name(books):
    search = input("Enter the book name: ").lower()

    found = False

    for book in books.values():
        if book["name"].lower() == search:
            print("\n Result")
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")
            found = True

    if not found:
        print("Book was not found.")


def search_genre(books):
    search = input("Enter the book genre: ").lower()

    found = False

    for book in books.values():
        if book["genre"].lower() == search:
            print("\n Result")
            print(f"Name:{book['name']}")
            print(f"Genre:{book['genre']}")
            print(f"Year:{book['year']}")
            found = True
    
    if not found:
        print("Book was not found.")


def search_year(books):
    search = input("Enter the book publication year ").lower()

    found = False

    for book in books.values():
        if book["year"].lower() == search:
            print("\n")
            print(f"Name:{book['name']}")
            print(f"Genre:{book['genre']}")
            print(f"Year:{book['year']}")
            found = True
    
    if not found:
        print("Book was not found.")

def search_books(books):
    width = 16
    text = "SEARCH BOOKS"
    print("-" * width)
    print(f"| {text} |")
    print("-" * width)
    print("1. Search the book by name")
    print("2. Search the book by genre")
    print("3. Search the book by publication year")
    
    choice = input("\n How would you like to search the book? ")
    
    if choice == "1": 
        search_name(books)

    elif choice == "2":
        search_genre(books)

    elif choice == "3":
        search_year(books)

    else:
        print("Invalid choice")

search_books(Books) 