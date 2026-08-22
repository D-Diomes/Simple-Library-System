def add_book(books):
    print("\n===== ADD BOOK =====")

    name = input("Enter the book name: ")
    genre = input("Enter the book genre: ")
    year = int(input("Enter the publication year: "))

    book_number = len(books) + 1
    book_id = f"book{book_number}"

    books[book_id] = {
        "name": name,
        "genre": genre,
        "year": year
    }

    print("\nBook has been added!")
    print(f"Name: {name}")
    print(f"Genre: {genre}")
    print(f"Year: {year}")
