from projects.models import Project
from rest_framework import viewsets
from rest_framework.filters import BaseFilterBackend, DjangoFilterBackend

from .models import Task
from .filters import TaskFilterByField, TaskFilterByPermissions
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""
    filter_class = TaskFilterByField
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = TaskFilterByPermissions, DjangoFilterBackend
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', )

