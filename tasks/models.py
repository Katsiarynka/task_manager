from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from projects.models import Project
from task_manager.models import TimeStampedModel

STATUS_WAITING = 1
STATUS_IN_PROGRESS = 2
STATUS_CODE_REVIEW = 3
STATUS_TESTING = 4
STATUS_COMPLETED = 5
STATUS_CHOICES = (
    (STATUS_WAITING, _('Waiting')),
    (STATUS_IN_PROGRESS, _('In Progress')),
    (STATUS_CODE_REVIEW, _('Code Review')),
    (STATUS_TESTING, _('Testing')),
    (STATUS_COMPLETED, _('Completed')),
)


class Task(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, null=True)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    project = models.ForeignKey(Project, null=True, blank=True)
    due = models.DateField(blank=True, null=True)
    started = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name