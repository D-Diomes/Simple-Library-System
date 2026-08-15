books = ["science", "math", "ap"]

to_remove = input("Enter item to delete: ")

books = [x for x in books if x != to_remove]

print("Updated books:", books)