import django_filters
from rest_framework_filters import AllLookupsFilter

from tasks.models import Task
from users.models import User


class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ('status', 'assigned', 'project', 'name', 'due', 'started', 'completed', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update({'to_field_name': User.USERNAME_FIELD})
