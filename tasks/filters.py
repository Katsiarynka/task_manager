import django_filters
from projects.models import Project
from rest_framework.filters import BaseFilterBackend

from .models import Task
from users.models import User


class TaskFilterByField(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ('status', 'assigned', 'project', 'name', 'due', 'started', 'completed', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update({'to_field_name': User.USERNAME_FIELD})


class TaskFilterByPermissions(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        data = {}
        if request.user.developer:
            projects = Project.objects.filter(users__in=[request.user.id])
            data = {'project__in': projects.values_list('id', flat=True)}
        return queryset.filter(**data)
