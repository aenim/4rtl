from rest_framework.permissions import BasePermission

class IsAllowedToWrite(BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type == "Author"

class IsAllowedToRead(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.is_allowed_to_read == "YES"