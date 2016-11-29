from projects.permissions import ProjectManagerOrReadOnly
from rest_framework import viewsets

from .models import Project
from .filters import ProjectFilter
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """API endpoint for listing projects."""
    queryset = Project.objects.order_by('-release')
    serializer_class = ProjectSerializer
    filter_class = ProjectFilter
    permission_classes = [ProjectManagerOrReadOnly]
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'start', 'release')


