from rest_framework import viewsets
from rest_framework.views import APIView

from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet, APIView):
    """API endpoint for listing users."""
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.select_related().order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    permission_classes = UserPermission,

    def perform_create(self, serializer):
        serializer.save(role_name=self.request.data.get('role_name', None))


