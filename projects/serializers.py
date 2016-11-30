from rest_framework import serializers
from rest_framework.reverse import reverse
from users.models import ROLE_DEVELOPER, ROLE_MANAGER
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    role_users = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start', 'release', 'links', 'role_users')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('project-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

    def get_role_users(self, obj):
        users = obj.users.all()
        return {
            'managers': users.filter(role__name=ROLE_MANAGER).values('id', 'username'),
            'developers': users.filter(role__name=ROLE_DEVELOPER).values('id', 'username')
        }

    def validate(self, attrs):
        start = attrs.get('start')
        release = attrs.get('release')
        if release and start and release < start:
            raise serializers.ValidationError(
                {"release": "Release date cannot be before start date"})
        return attrs


