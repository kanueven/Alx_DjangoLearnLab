from django.urls import path

from LibraryProject.relationship_app.member_view import member_view, librarian_view, admin_view
from .views import delete_book,add_book,edit_book, list_books, LibraryDetailView, LoginView,LogoutView
from . import views

urlpatterns = [
    path('', list_books, name='home'),  # home page shows all books
    path('books/', list_books, name='book-list'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
    #authentication views url
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'), 
    
    # Role-based URLs
    path('admin-page/', admin_view.admin_view, name='admin-page'),
    path('librarian-page/', librarian_view.librarian_view, name='librarian-page'),
    path('member-page/', member_view.member_view, name='member-page'),
    
    path('book/add/', add_book, name='add-book'),
    path('book/edit/<int:pk>/', edit_book, name='edit-book'),
    path('book/delete/<int:pk>/', delete_book, name='delete-book'),
]

