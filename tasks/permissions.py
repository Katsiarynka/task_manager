from rest_framework.permissions import BasePermission, SAFE_METHODS

ALLOWED_DEVELOPER_METHODS = SAFE_METHODS + ['PUT']


class TaskManagerOrProjectsDeveloper(BasePermission):

    def has_permission(self, request, view):
        if request.user.developer and request.method in ALLOWED_DEVELOPER_METHODS or \
                request.user.manager:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.developer and request.method in ALLOWED_DEVELOPER_METHODS or \
                request.user.manager:
            return True
        return False
