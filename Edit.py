def edit_book(books):
    search = input("Enter the name of the book you want to edit: ").lower()

    found = False

    for book in books.values():
        if book["name"].lower() == search:

            print("\n===== CURRENT BOOK =====")
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")

            print("\n===== EDIT BOOK =====")

            new_name = input("Enter the new book name: ")
            new_genre = input("Enter the new genre: ")
            new_year = int(input("Enter the new publication year: "))

            book["name"] = new_name
            book["genre"] = new_genre
            book["year"] = new_year

            print("\nBook has been updated!")
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")

            found = True
            break

    if not found:
        print("Book was not found.")