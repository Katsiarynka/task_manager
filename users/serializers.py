from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User, Role, ROLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'role')

    def get_role(self, obj):
        return str(obj.role)

    def get_links(self, obj):
        username = obj.get_username()
        username_field = User.USERNAME_FIELD
        request = self.context['request']
        return {
            'self': reverse('user-detail', kwargs={username_field: username}, request=request),
        }


class UserRegistration(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def validate_role_name(self, role_name=""):
        choices = dict((key.lower(), value) for key, value in ROLE_CHOICES)
        if not (role_name.lower() in choices.keys()):
            raise serializers.ValidationError("Role should be like {}.".format(",".join(choices)))
        return choices[role_name.lower()]

    def create(self, validated_data):
        role_name = validated_data.pop('role_name')
        role_name = self.validate_role_name(role_name)
        validated_data['role'] = Role.objects.get_or_create(name=role_name)[0]
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
