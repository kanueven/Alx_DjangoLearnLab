from django.urls import path
from .views import RegisterView, LoginView, ProfileView,FollowerUserView,UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("follow/<int:user_id>/", FollowerUserView.as_view()),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view()),
]
