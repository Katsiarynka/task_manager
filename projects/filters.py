import rest_framework_filters as filters

from .models import Project


class ProjectFilter(filters.FilterSet):
    name = filters.AllLookupsFilter(name='name')
    start = filters.AllLookupsFilter(name='start')
    release = filters.AllLookupsFilter(name='release')

    class Meta:
        model = Project

    def filter_queryset(self, request, queryset, view):
        filter = {}
        if request.user.developer:
            project_ids = Project.objects.filter(users__id_in=[request.user_id])
            filter['project__id_in'] = project_ids.values_list('id', flat=True)
        return queryset.filter(**filter)


