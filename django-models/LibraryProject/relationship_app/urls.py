# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    # Function-based view: lists all books
    path('books/', list_books, name='list_books'),

    # Class-based view: details for a specific library with its books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]