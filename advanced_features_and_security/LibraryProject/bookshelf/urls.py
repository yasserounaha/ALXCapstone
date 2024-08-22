# urls.py in bookshelf

from django.urls import path
from . import views

urlpatterns = [
    path('edit_book/<int:pk>/', views.EditBookView.as_view(), name='edit_book'),
    path('view_book/<int:book_id>/', views.view_book, name='view_book'),
    path('create_book/', views.create_book, name='create_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    # other URL patterns
]
