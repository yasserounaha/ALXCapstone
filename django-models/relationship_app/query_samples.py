from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        # Get the library
        library = Library.objects.get(name=library_name)
        # Retrieve the librarian associated with the library
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

