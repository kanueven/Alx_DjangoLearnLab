from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
#Function-based views and class-based views

#function-based views
def list_books(request):
    #fetch all books from the database
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


#class-based views, that displays details for a specific library, listing all books available in that library.
#Utilize Django’s ListView or DetailView to structure this class-based view.
class LibraryDetailsView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
#login view placeholder
def login_view(request):
    return render(request, 'relationship_app/login.html')
def logout_view(request):
    return render(request, 'relationship_app/logout.html')
def register_view(request):
    return render(request, 'relationship_app/register.html')