from rest_framework.permissions import BasePermission, SAFE_METHODS


class ProjectManagerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.developer and request.method in SAFE_METHODS or \
                request.user.manager:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.id in obj.users and request.method in SAFE_METHODS or \
                request.user.manager:
            return True
        return False
