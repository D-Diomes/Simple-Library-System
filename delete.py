def delete_book(books):
    search = input("Enter the name of the book you want to delete: ").lower()

    found = False

    for book_id, book in list(books.items()):
        if book["name"].lower() == search:
            print("\n===== BOOK FOUND =====")
            print(f"Name: {book['name']}")
            print(f"Genre: {book['genre']}")
            print(f"Year: {book['year']}")

            confirm = input("\nAre you sure you want to delete this book? (yes/no): ").lower()

            if confirm == "yes":
                del books[book_id]
                print("\nBook has been deleted!")
            else:
                print("\nBook was not deleted.")

            found = True
            break

    if not found:
        print("Book was not found.")
