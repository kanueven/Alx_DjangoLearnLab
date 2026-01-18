from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
#Function-based views and class-based views

#function-based views
def list_books(request):
    #fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#class-based views, that displays details for a specific library, listing all books available in that library.
#Utilize Django’s ListView or DetailView to structure this class-based view.
class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'