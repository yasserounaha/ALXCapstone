from django.urls import path , include
from .views import UserLoginView, UserLogoutView, UserRegisterView,list_books, LibraryDetailView , home
from . import views
urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('register/', UserRegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('login/', UserLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', home, name='home'),  # Root URL
     path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
]
