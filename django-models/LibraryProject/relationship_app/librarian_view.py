from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .views import is_librarian

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, "relationship_app/librarian_dashboard.html")