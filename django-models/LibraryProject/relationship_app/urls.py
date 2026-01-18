from django.urls import path
from .views import list_books, LibraryDetailView, LoginView,LogoutView
from . import views

urlpatterns = [
    path('', list_books, name='home'),  # home page shows all books
    path('books/', list_books, name='book-list'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'), 
]
