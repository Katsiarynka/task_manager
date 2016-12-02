from django.db import models
from django.contrib.auth.models import AbstractUser
from task_manager.models import TimeStampedModel

ROLE_MANAGER = 'Manager'
ROLE_DEVELOPER = 'Developer'
ROLE_CHOICES = (
    (ROLE_MANAGER, ROLE_MANAGER),
    (ROLE_DEVELOPER, ROLE_DEVELOPER),
)


class Role(models.Model):
    name = models.CharField(max_length=63, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, null=True)

    @property
    def manager(self):
        return self.role.name == ROLE_MANAGER

    @property
    def developer(self):
        return self.role.name == ROLE_DEVELOPER
