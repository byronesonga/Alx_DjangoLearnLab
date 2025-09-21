from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is Admin
def is_admin(user):
    return user.is_authenticated and user.role == "Admin"

@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")
