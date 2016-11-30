from django.db import models

from users.models import User
from task_manager.models import TimeStampedModel


class Project(TimeStampedModel):
    """Project information."""
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    start = models.DateField()
    release = models.DateField(null=True, blank=True)
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.name or self.description
