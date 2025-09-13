Code Executed in Django Shell
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> print(book.id, book.title, book.author, book.publication_year)
Output	
1 1984 George Orwell 1949
Explanation
•	Book.objects.get(id=1) fetches the Book object with primary key 1 from the database.
•	The retrieved object is stored in the variable book.
•	Printing its attributes confirms that the record matches the data created earlier.
