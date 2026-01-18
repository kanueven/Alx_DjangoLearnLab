from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('',views.list_books, name='home'),
    #for the function-based view
    path('books/', views.list_books, name='book-list'),
    #for the class-based view(expects a pk parameter)
    path('library/<int:pk>/', views.LibraryDetails.as_view(), name='library-detail'),
]
