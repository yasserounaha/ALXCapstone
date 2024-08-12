# retrieve.md

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book)
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
