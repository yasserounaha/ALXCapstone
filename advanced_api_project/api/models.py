from django.db import models

# The Author model represents a writer or creator of books.
class Author(models.Model):
    # The name of the author. This is a CharField with a maximum length of 100 characters.
    name = models.CharField(max_length=100)

    # String representation of the Author object, returns the author's name.
    def __str__(self):
        return self.name

# The Book model represents a book written by an author.
class Book(models.Model):
    # The title of the book. This is a CharField with a maximum length of 200 characters.
    title = models.CharField(max_length=200)

    # The year the book was published. This is an IntegerField.
    publication_year = models.IntegerField()

    # The author of the book. This is a ForeignKey that links to the Author model.
    # A single author can have many books (one-to-many relationship).
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    # String representation of the Book object, returns the book's title.
    def __str__(self):
        return self.title
