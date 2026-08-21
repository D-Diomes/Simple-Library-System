Books = {
    "book1": {
        "Name": "Punisher Max: In the Beginning",
        "Genre": "Crime",
        "year": 2004
    },
    "book2": {
        "Name": "Captain America: The Winter Soldier",
        "Genre": "Adventure",
        "year": 2005
    },
    "book3": {
        "Name": "Black Widow: The Name of the Rose",
        "Genre": "Action",
        "year": 2010
    }
}


def Edit():
    print("Available books:")
    for book in Books:
        print(book)

    book = input("Enter the book you want to edit: ")

    if book not in Books:
        print("Book not found.")
        return

    print("\nWhat do you want to edit?")
    print("1. Edit book name")
    print("2. Edit book genre")
    print("3. Edit book year")

    num = int(input("Enter your choice: "))

    if num == 1:
        new_name = input("Enter new book name: ")
        Books[book]["Name"] = new_name

    elif num == 2:
        new_genre = input("Enter new book genre: ")
        Books[book]["Genre"] = new_genre

    elif num == 3:
        new_year = int(input("Enter new book year: "))
        Books[book]["year"] = new_year

    else:
        print("Invalid choice.")
        return

    print("\nBook successfully updated!")
    print(Books[book])


while True:
    Edit()
    break