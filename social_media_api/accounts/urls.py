from django.urls import path
from .views import RegisterView, CustomLoginView
from rest_framework.routers import DefaultRouter
from .views import follow_user, unfollow_user
from . import views
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
     path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
