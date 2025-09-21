from rest_framework import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()          # fetch all Book records
    serializer_class = BookSerializer      # use BookSerializer to serialize them

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Book instances.
    Provides `list`, `create`, `retrieve`, `update`, and `destroy` actions automatically.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer