from django.urls import path , include
from .views import BookList , BookViewSet
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]