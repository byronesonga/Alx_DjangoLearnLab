from django.http import HttpResponse
from .models import Book

# Create your views here.
# relationship_app/views.py


def list_books(request):
    # Fetch all books with related author objects
    books = Book.objects.select_related('author').all()
    
    # Build a simple text response
    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")
    
    return HttpResponse("<br>".join(output))

# relationship_app/views.py
from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # custom template
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        # Get the base context
        context = super().get_context_data(**kwargs)
        # Add related books for this library
        context["books"] = self.object.book_set.all()
        return context
