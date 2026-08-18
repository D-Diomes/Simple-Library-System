books = {
    1: "Punisher Max: In the Beginning",
    2: "Captain America: The Winter Soldier",
    3: "Black Widow: The Name of the Rose"
}

for n, book in books.items():
    print(n, book)

choice = int(input("Delete book number: "))

if choice in books:
    del books[choice]
    print("Book deleted!")
else:
    print("Book not found!")

print(books)