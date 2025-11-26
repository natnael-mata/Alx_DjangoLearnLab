# Delete a Book instance

```python
from bookshelf.models import Book

# Retrieve the book you want to delete
book = Book.objects.get(id=1)

# Delete the book
book.delete()

# Verify deletion
Book.objects.filter(id=1)
# Expected output: <QuerySet []>  (empty queryset, book deleted)
