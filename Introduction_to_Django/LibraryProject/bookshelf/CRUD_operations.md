
------------
Ctrl click to launch VS Code Native REPL
Python 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)


#object Creation
>>> from bookshelf.models import Book
>>> book = Book.objects.create(
author="George Orwell",
    publication_year=1949
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
)
... )
>>> print(books)

#Object Retriving

>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949

#Uppdating

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four
#Deleteing
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> 