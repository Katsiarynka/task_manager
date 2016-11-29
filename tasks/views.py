from rest_framework import viewsets

from .models import Task
from .filters import TaskFilter
from .serializers import TaskSerializer


class TaskViewSet( viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', )

