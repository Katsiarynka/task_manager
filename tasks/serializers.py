from rest_framework import serializers
from rest_framework.reverse import reverse

from users.models import User
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()
    assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD,
                                            queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status_display', 'order',
                  'assigned', 'project', 'links', 'started', 'due', 'completed')

    def get_status_display(self, obj):
        return obj.get_status_display()

    def get_links(self, obj):
        request = self.context['request']
        links = {
            'self': reverse('task-detail', kwargs={'pk': obj.pk}, request=request),
            'project': None,
            'assigned': None
        }

        if obj.project_id:
            links['project'] = reverse('project-detail',
                                       kwargs={'pk': obj.project_id}, request=request)
        if obj.assigned:
            username_field = User.USERNAME_FIELD
            links['assigned'] = reverse('user-detail',
                                        kwargs={username_field: obj.assigned}, request=request)
        return links