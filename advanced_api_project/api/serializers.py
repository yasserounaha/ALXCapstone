from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializer for the Book model.
# It serializes all fields of the Book model and includes validation for publication_year.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        # Specify the model to serialize.
        model = Book

        # Specify that all fields in the model should be included in the serialization.
        fields = '__all__'

    # Custom validation method for publication_year.
    # Ensures that the publication year is not in the future.
    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model.
# It includes the author's name and a nested serialization of the books written by the author.
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer for the books related to the author.
    # This uses the BookSerializer to serialize the books and sets many=True because an author can have multiple books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        # Specify the model to serialize.
        model = Author

        # Specify the fields to be included in the serialization: the author's name and the nested books.
        fields = ['name', 'books']
