from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.developer and request.method in SAFE_METHODS or \
                request.user.manager:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.developer and request.method in SAFE_METHODS or \
                request.user.manager:
            return True
        return False
