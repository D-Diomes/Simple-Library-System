books = []

def add_book():
    title = input ("Enter book title:")
    author = input ("Enter author name:")

    book = {
    "title": title,
     "author": author   
 }

    books.append(book)
print ("Book Added Successfully!")