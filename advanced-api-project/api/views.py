from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Book
from .serializers import BookSerializer

# Create your views here.
#Implement a set of generic views for the Book model to handle CRUD operations
#retrieve all books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Must include these for filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search
    search_fields = ['title', 'author__name']

    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

#A DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated users

#createview for creating a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow logged user to create a book
    

#UpdateView for updating an existing book
class BookUpdateView(generics.UpdateAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow logged user to update a book
    
#DeleteView for deleting a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]