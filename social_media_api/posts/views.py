from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Assign the post to the current user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Assign the comment to the current user
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    """
    Create a view in the posts app that generates a feed based on the posts from users 
    that the current user follows. This view should return posts ordered by creation date, 
    showing the most recent posts at the top.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the users the current user is following
        following_users = self.request.user.following.all()
        # Return posts from followed users, ordered by creation date (most recent at the top)
        return Post.objects.filter(author__in=following_users).order_by('-published_date')


class FollowUserView(GenericAPIView):
    """
    A view to allow the current user to follow another user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=200)


class UnfollowUserView(GenericAPIView):
    """
    A view to allow the current user to unfollow another user.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=400)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=200)