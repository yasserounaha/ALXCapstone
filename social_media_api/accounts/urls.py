from django.urls import path
from .views import RegisterView, CustomLoginView
from rest_framework.routers import DefaultRouter
from . import views
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
