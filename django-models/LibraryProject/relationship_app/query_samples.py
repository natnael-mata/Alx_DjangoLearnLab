# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def query_books_by_author(author_name):
    """
    Retrieves all books written by the specified author.
    """
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2. List all books in a library
def list_books_in_library(library_name):
    """
    Retrieves all books stored in the specified library.
    """
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    """
    Retrieves the librarian assigned to the specified library.
    """
    library = Library.objects.get(name=library_name)
    Librarian.objects.get(library=library)
     # One-to-one relationship
    return librarian


# --- SAMPLE USAGE (for Django shell or debugging) ---

if __name__ == "__main__":
    # Query examples (will run when script executes)
    print("Books by Author:")
    for b in query_books_by_author("J.K. Rowling"):
        print(b.title)

    print("\nBooks in Library:")
    for b in list_books_in_library("Central Library"):
        print(b.title)

    print("\nLibrarian for Library:")
    librarian = get_librarian_for_library("Central Library")
    print(librarian.name)
