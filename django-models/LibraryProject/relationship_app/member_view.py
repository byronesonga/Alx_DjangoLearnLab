from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .views import is_member

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, "relationship_app/member_dashboard.html")