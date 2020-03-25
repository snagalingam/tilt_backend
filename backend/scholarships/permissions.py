from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allwoed to admin users
        return bool(request.user and request.user.is_staff)
