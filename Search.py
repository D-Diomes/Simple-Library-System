def search_book(books):
    search = input("Enter the book name: ").lower()

    found = False

    for book in books.values():
        if book["name"].lower() == search:
            print("\n The book has been found!")
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
            print("\n The book has been found!")
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
            print("\n The book has been found!")
            print(f"Name:{book['name']}")
            print(f"Genre:{book['genre']}")
            print(f"Year:{book['year']}")
            found = True
    
    if not found:
        print("Book was not found.")

 