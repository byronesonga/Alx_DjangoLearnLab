1. Create Operation
>>> from bookshelf.models import Book
>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
>>> print(book.id, book.title)
Output:
1 1984
2. Retrieve Operation
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> print(book.id, book.title, book.author, book.publication_year)
Output:
1 1984 George Orwell 1949
3. Update Operation
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.id, book.title)
Output:
1 Nineteen Eighty-Four
4. Delete Operation
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.delete()
Output:
(1, {'bookshelf.Book': 1})
Summary
•	Create: Added a new Book record.
•	Retrieve: Queried the created record.
•	Update: Modified the record’s title.
•	Delete: Removed the record from the database.
This completes the full cycle of CRUD operations on the Book model.
