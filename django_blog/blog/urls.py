from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView,CommentCreateView,CommentUpdateView,CommentDeleteView,SearchResults,PostByTagListView


urlpatterns = [
    path('', views.home, name='blog-home'),
    # authenitfication urls
    path('register/', views.registerPage, name='blog-register'),
    path('profile/', views.profile, name='blog-profile'),
    path('login/', views.login_view, name='blog-login'),
    path('logout/', views.logout_view, name='blog-logout'),
    
    # crud urls for posts
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
     # Comment URLs
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    
    #search url
    path('search/', SearchResults.as_view(), name='search-results'),
    
    # Posts by tag
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]

