from django.urls import path
from .views import VlogListView, add_vlog, edit_vlog, delete_vlog

urlpatterns = [
    path('vlogs/', VlogListView.as_view(), name='vlog-list'),
    path('vlogs/add/', add_vlog, name='add-vlog'),
    path('vlogs/edit/<int:pk>/', edit_vlog, name='edit-vlog'),
    path('vlogs/delete/<int:pk>/', delete_vlog, name='delete-vlog'),
]
