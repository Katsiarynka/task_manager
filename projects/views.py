from projects.permissions import ProjectPermissions
from rest_framework import viewsets
from rest_framework.filters import DjangoFilterBackend

from .models import Project
from .filters import ProjectFilterByField, ProjectFilterByRole
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint for listing projects."""
    queryset = Project.objects.order_by('-release')
    serializer_class = ProjectSerializer
    permission_classes = ProjectPermissions,
    filter_backends = ProjectFilterByRole, DjangoFilterBackend
    filter_class = ProjectFilterByField
    filter_fields = Project._meta.get_fields()
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'start', 'release')


