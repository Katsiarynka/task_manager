from rest_framework.permissions import BasePermission, SAFE_METHODS


class ProjectPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.manager or request.user.developer and request.method in SAFE_METHODS:
            return True
        return False
