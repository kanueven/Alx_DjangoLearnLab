from django.urls import path
from django.http import HttpResponse
from .views import list_books, LibraryDetails
from LibraryProject.relationship_app import views

urlpatterns = [
    path('',views.list_books, name='home'),
    #for the function-based view
    path('books/', views.list_books, name='book-list'),
    #for the class-based view(expects a pk parameter)
    path('library/<int:pk>/', views.LibraryDetails.as_view(), name='library-detail'),
    #login
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('register/',views.register_view, name='register')
]
