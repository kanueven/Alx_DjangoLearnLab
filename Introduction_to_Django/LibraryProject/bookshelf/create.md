# CRUD Operations for Book Model
<!-- Markdown uses ``` for code blocks. -->

## Create

```python
from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
book
