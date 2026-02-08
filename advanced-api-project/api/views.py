from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer

# Create your views here.
#Implement a set of generic views for the Book model to handle CRUD operations
#retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['author', 'publication_year']  # Allow filtering by author and published date 
    search_fields = ['title', 'author']  # Allow searching by title and author
    ordering_fields = ['publication_year','title']  # Allow ordering by published date
#A DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

#createview for creating a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Allow logged user to create a book
    

#UpdateView for updating an existing book
class BookUpdateView(generics.UpdateAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Allow logged user to update a book
    
#DeleteView for deleting a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]