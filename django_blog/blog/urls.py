from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='blog-home'),
    # authenitfication urls
    path('register/', views.registerPage, name='blog-register'),
    path('profile/', views.profile, name='blog-profile'),
    path('login/', views.login_view, name='blog-login'),
    path('logout/', views.logout_view, name='blog-logout'),
    
    # crud urls
     path('', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

