from django.contrib import admin

# Register your models here.
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .views import is_admin

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "relationship_app/admin_dashboard.html")