# api/views.py
from rest_framework import generics
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny
class BookFilter(filters.FilterSet):
    # Define custom filters here
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title']
class BookListView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to list books
def perform_create(self, serializer):
        # Custom logic before saving the book instance
        # For example, you can modify the data here
        serializer.save()
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict updates and deletes to authenticated users

def perform_update(self, serializer):
        # Custom logic before updating the book instance
        # For example, you can modify the data here
        serializer.save()