from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path('', list_books, name='home'),  # home page shows all books
    path('books/', list_books, name='book-list'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
    path('login/', login_view, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('register/', register_view.as_view(), name='register'),
]
