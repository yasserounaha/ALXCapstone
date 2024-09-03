# api/urls.py
from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve, update, delete
]
