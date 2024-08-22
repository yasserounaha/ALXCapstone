from django.urls import path
from .views import UserLoginView, UserLogoutView, UserRegisterView, list_books, LibraryDetailView, home, admin_view, librarian_view, member_view, AddBookView, EditBookView, DeleteBookView, register

urlpatterns = [
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', EditBookView.as_view(), name='edit_book'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
