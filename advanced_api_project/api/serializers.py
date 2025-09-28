from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"   # include all fields: title, publication_year, author

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year {value} cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Nest BookSerializer to show related books
    books = BookSerializer(many=True, read_only=True)  
    # related_name="books" in Book model makes this possible

    class Meta:
        model = Author
        fields = ["name", "books"]   # include only author name + related books
