# Update a Book instance

```python
from bookshelf.models import Book

# Retrieve the book you want to update
book = Book.objects.get(id=1)

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
print(book.title, book.author, book.publication_year)
# Expected output: Nineteen Eighty-Four John Doe 2025
