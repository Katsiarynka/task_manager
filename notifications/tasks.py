import json
import logging

from django_celery_beat.models import IntervalSchedule, PeriodicTask
from tasks.models import Task
from celery import Celery

from users.models import User
from notifications.models import MessageWorker, Email


app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    schedule, created = IntervalSchedule\
        .objects.get_or_create(every=3, period=IntervalSchedule.HOURS,)
    PeriodicTask.objects.get_or_create(interval=schedule, name='notifications.check_new_tasks',
                                       task='notifications.check_new_tasks',
                                       args=json.dumps(['every 3 hours']),)


@app.task(bind=True, name='notifications.check_new_tasks')
def check_new_tasks(self, period="from db"):
    try:
        last_worker = MessageWorker.objects.latest('created')
        last_started_at = last_worker.created
        worker = MessageWorker.objects.create()
    except MessageWorker.DoesNotExist:
        worker = MessageWorker.objects.create()
        last_started_at = worker.created

    emails_was_sent = 0
    subject = "Generated notification about assigned tasks to you for {}".format(period)
    text = "You have next assigned tasks since {}:" .format(last_started_at)
    created_tasks = Task.objects.filter(created__gt=last_started_at)
    user_ids = set(i for i in created_tasks.values_list('assigned', flat=True) if i)
    for user in User.objects.filter(id__in=user_ids):
        try:
            user_tasks = created_tasks.filter(assigned=user)
            msg_body = "{0}\n {1}".format(text, "\n".join(str(t) for t in user_tasks))
            email = Email.objects.create(user=user, subject=subject, text=msg_body)
            email.send()
            emails_was_sent += 1
        except Exception as e:
            logging.error(e)

    worker.sent_emails = emails_was_sent
    worker.save()

