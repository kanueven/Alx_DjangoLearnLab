from django.urls import path
from .views import VlogListView, add_vlog, book_list, edit_vlog, delete_vlog

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('vlogs/', VlogListView.as_view(), name='vlog-list'),
    path('vlogs/add/', add_vlog, name='add-vlog'),
    path('vlogs/edit/<int:pk>/', edit_vlog, name='edit-vlog'),
    path('vlogs/delete/<int:pk>/', delete_vlog, name='delete-vlog'),
]
