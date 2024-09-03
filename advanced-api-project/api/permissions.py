# api/permissions.py
from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors to edit or delete their own books.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the author of the book
        return obj.author == request.user
