from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow write permissions only if the user is the owner of the object
        return obj.user == request.user