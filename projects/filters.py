from rest_framework.filters import BaseFilterBackend
from rest_framework_filters import FilterSet, AllLookupsFilter

from .models import Project


class ProjectFilterByRole(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter = {}
        if request.user.developer:
            projects = Project.objects.filter(users__in=[request.user.id])
            filter['id__in'] = projects.values_list('id', flat=True)
        return queryset.filter(**filter)


class ProjectFilterByField(FilterSet):
    name = AllLookupsFilter(name='name')
    start = AllLookupsFilter(name='start')
    release = AllLookupsFilter(name='release')

    class Meta:
        model = Project



