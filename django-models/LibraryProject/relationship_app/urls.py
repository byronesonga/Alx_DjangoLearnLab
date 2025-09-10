# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import admin_view, librarian_view, member_view



urlpatterns = [
    # Function-based view: lists all books
    path('books/', list_books, name='list_books'),

    # Class-based view: details for a specific library with its books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    path("", views.home_view, name="home"),

    # Class-based authentication views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Registration still custom (since Django doesn’t ship one)
    path("register/", views.register_view, name="register"),
]

urlpatterns = [
    path("books/", views.list_books, name="list_books"),
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/<int:book_id>/edit_book/", views.edit_book, name="edit_book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete_book"),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path("admin-dashboard/", admin_view.admin_dashboard, name="admin_dashboard"),
    path("librarian-dashboard/", librarian_view.librarian_dashboard, name="librarian_dashboard"),
    path("member-dashboard/", member_view.member_dashboard, name="member_dashboard"),
]



