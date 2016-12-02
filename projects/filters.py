import django_filters
from rest_framework.filters import BaseFilterBackend

from .models import Project


class ProjectFilterByRole(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter = {}
        if request.user.developer:
            projects = Project.objects.filter(users__in=[request.user.id])
            filter['id__in'] = projects.values_list('id', flat=True)
        return queryset.filter(**filter)


class ProjectFilterByField(django_filters.FilterSet):

    class Meta:
        model = Project
        fields = ['name', 'description', 'start', 'release']



