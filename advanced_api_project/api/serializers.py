from rest_framework import serializers
from .models import Author, Book
from datetime import date

 # Create a BookSerializer that serializes all fields of the Book model.
# Create an AuthorSerializer that includes:
# The name field.
# A nested BookSerializer to serialize the related books dynamically.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        #Add custom validation to the BookSerializer to ensure the publication_year is not in the future.
        def validate_pubblication_year(self,value):
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value
            
        
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']