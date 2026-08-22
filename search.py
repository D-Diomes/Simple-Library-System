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
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")
            found = True

    if not found:
        print("Book was not found.")


def search_year(books):
    search = input("Enter the book publication year: ")

    found = False

    for book in books.values():
        # book["year"] is stored as an int, so compare it as a string
        # instead of calling .lower() on it (which caused a crash)
        if str(book["year"]) == search:
            print("\n Result")
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")
            found = True

    if not found:
        print("Book was not found.")
