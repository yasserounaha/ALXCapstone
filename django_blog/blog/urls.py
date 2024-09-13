from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comment/new/', views.add_comment, name='add-comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
]

