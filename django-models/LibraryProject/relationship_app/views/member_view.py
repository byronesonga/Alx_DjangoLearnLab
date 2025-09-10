from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is Member
def is_member(user):
    return user.is_authenticated and user.role == "Member"

@user_passes_test(is_member)
def member_dashboard(request):
    return HttpResponse("Welcome to the Member Dashboard!")
