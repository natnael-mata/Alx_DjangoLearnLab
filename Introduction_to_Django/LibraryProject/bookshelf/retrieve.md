#1. Printing Book Objects
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
#2. Output

#1984 George Orwell 1949