from django.shortcuts import render
from .decorators import role_required

@role_required(allowed_roles=['Admin'])
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html', {})
