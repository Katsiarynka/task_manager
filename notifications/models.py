import smtplib
from email.mime.text import MIMEText

from django.conf import settings
from django.db import models
from task_manager.models import TimeStampedModel
from users.models import User

SENT = "sent"
FAILED = "failed"
INITIALIZING = 'initializing'


class EmailValidation(Exception):
    pass


class Email(TimeStampedModel):
    user = models.ForeignKey(User, null=True, related_name='recipient_user')
    subject = models.CharField(max_length=255, blank=True, null=True)
    sender = models.EmailField(null=False, blank=True, max_length=255)
    recipient = models.EmailField(null=False, blank=True, max_length=255)
    status = models.CharField(max_length=255, default=INITIALIZING)
    text = models.TextField(null=True, blank=True, default='')
    error_message = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.status

    def validate_email(self):
        if not self.subject:
            raise EmailValidation("Subject is required")
        if not self.recipient and not(self.user and self.user.email):
            raise EmailValidation("Recipient is required")
        if not self.text:
            raise EmailValidation("text is required")

    def send(self):
        self.validate_email()
        self.sender = self.sender or settings.SENDER_EMAIL
        self.recipient = self.recipient or self.user.email

        msg = MIMEText(self.text)
        msg['Subject'] = self.subject
        msg["From"] = self.sender
        msg['To'] = self.recipient
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        try:
            if not settings.TEST:
                server.ehlo()
                server.starttls()
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)
            self.status = SENT
        except Exception as e:
            self.status = FAILED
            self.error_message = e
        finally:
            server.quit()
            self.save()


class MessageWorker(TimeStampedModel):
    sent_emails = models.IntegerField(null=True, blank=True, default=0)

    def __unicode__(self):
        return "emails: {0:d}".format(self.sent_emails or 0)
