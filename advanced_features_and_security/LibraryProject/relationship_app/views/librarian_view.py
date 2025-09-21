from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is Librarian
def is_librarian(user):
    return user.is_authenticated and user.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Welcome to the Librarian Dashboard!")
