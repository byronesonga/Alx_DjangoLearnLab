Code Executed in Django Shell
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.delete()
Output
(1, {'bookshelf.Book': 1})
Explanation
•	Book.objects.get(id=1) retrieves the Book object with primary key 1.
•	book.delete() removes the record from the database.
•	The output (1, {'bookshelf.Book': 1}) indicates that 1 object from the Book model was deleted successfully.
