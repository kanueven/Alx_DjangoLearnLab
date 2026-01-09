from bookshelf.models import Book

# create a book instance
book = Book(title = "1984", author = "George Orwell",publication_year = 1949)
book.save()
book
<!--  output -->
<!-- <Book: Book object (1)> -->

# Get the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
<!-- ouput -->
<!-- <Book: Book object (1)> -->

# retrieve all books
Book.objects.all()

<!-- expected output -->
<!-- <QuerySet [<Book: Book object (1)> -->

# retrieve books with id(1)
Book.objects.filter(id=1)
<!-- expected output -->
<!-- <QuerySet [<Book: Book object (1)>]> -->

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
<!-- output -->
<!-- <QuerySet []> -->