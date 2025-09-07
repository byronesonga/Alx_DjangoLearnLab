# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based view: lists all books
    path('books/', list_books, name='list_books'),

    # Class-based view: details for a specific library with its books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
