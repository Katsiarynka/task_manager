from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.manager or request.user == obj or \
                        request.user.developer and request.method in SAFE_METHODS:
            return True
        return False
