from projects.models import Project
from rest_framework import viewsets
from rest_framework.filters import BaseFilterBackend

from .models import Task
from .filters import TaskFilter
from .serializers import TaskSerializer


class TaskFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        data = {}
        if request.user.developer:
            projects = Project.objects.filter(users__in=[request.user.id])
            data = {'project__in': projects.values_list('id', flat=True)}
        return queryset.filter(**data)


class TaskViewSet( viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""
    filter_backends = TaskFilter,
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', )

