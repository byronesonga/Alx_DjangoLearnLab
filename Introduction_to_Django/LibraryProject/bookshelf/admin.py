from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # fields to display in list
    search_fields = ('title', 'author')                   # add search functionality
    list_filter = ('publication_year',)                    # add filters

admin.site.register(Book, BookAdmin)
