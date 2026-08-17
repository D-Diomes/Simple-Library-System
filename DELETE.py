books = ["science", "math", "ap"]

print("Current books:", books)

to_remove = input("Enter item to delete: ")

if to_remove in books:
    books.remove(to_remove)
    print("Item deleted!")
else:
    print("Item not found!")

print("Updated books:", books)