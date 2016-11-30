from rest_framework import serializers
from rest_framework.reverse import reverse
from django.core.validators import validate_email

from .models import User, Role, ROLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    role_name = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active',
                  'role_name', 'links', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'email': {'required': True},
        }

    def get_role_name(self, obj):
        return str(obj.role)

    def validate_email(self, email=None):
        if email:
            validate_email(email)
            exists = User.objects.filter(email=email)
            if exists.exists():
                raise serializers.ValidationError("This email is already in the system.")
        return email

    def validate_role_name(self, role_name=""):
        choices = {key.lower(): value for key, value in ROLE_CHOICES}
        if not (role_name.lower() in choices.keys()):
            roles = ",".join(choices.values())
            raise serializers.ValidationError("Role name should be like {}.".format(roles))
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

    def get_links(self, obj):
        return {'self': reverse('user-detail',
                                kwargs={User.USERNAME_FIELD: obj.get_username()},
                                request=self.context['request']),
                }
