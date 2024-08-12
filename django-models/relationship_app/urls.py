from django.urls import path , include
from .views import list_books, LibraryDetailView , home

urlpatterns = [
    path('', home, name='home'),  # Root URL
     path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]
