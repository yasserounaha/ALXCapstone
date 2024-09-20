from django.urls import path
from .views import RegisterView, CustomLoginView
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', views.CommentViewSet, basename='post-comments')
urlpatterns = router.urls
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
