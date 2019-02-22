from rest_framework.permissions import BasePermission

USERNAME_REPLACEMENT_GROUP = "username_replacement_admin"

class ReadOnlyByPublisherUser(BasePermission):
    """
    Custom Permission class to check user is a publisher user.
    """
    def has_permission(self, request, view):
        if request.method == 'GET':
                return request.user.groups.exists()
        return True

class CanReplaceUsername(BasePermission):
    """
    Grants access to the Username Replacement API for anyone in the group,
    including the service user.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name=USERNAME_REPLACEMENT_GROUP).exists()
