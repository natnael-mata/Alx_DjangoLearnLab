#1. Import the model
from bookshelf.models import Book

#2. Create Book Instance
book = Book.objects.create(
author="George Orwell",
    publication_year=1949
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
)

#3. Output