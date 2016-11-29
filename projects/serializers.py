from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start', 'release', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('project-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

    def validate(self, attrs):
        start = attrs.get('start')
        release = attrs.get('release')
        if release and start and release < start:
            raise serializers.ValidationError(
                {"release": "Release date should be more then start date"})
        return attrs


