from django.urls import path , include
from .views import UserLoginView, UserLogoutView, UserRegisterView,list_books, LibraryDetailView , home

urlpatterns = [
     path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', home, name='home'),  # Root URL
     path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]
