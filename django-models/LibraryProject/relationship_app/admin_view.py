from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .views import admin

@user_passes_test(admin)
def admin_dashboard(request):
    return render(request, "relationship_app/admin_dashboard.html")