Code Executed in Django Shell
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.id, book.title)
Output
1 Nineteen Eighty-Four
Explanation
•	Book.objects.get(id=1) retrieves the record with primary key 1.
•	The title field of the object is updated to "Nineteen Eighty-Four".
•	Calling book.save() writes the updated value back to the database.
•	Printing confirms that the title has been successfully updated.
