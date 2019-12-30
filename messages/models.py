from django.db import models

from model_utils.models import TimeStampedModel, SoftDeletableModel

# Create your models here.
from jobapply import models
from django.conf import settings
from django.template.defaultfilters import date as dj_date
from django.utils.timezone import localtime


class Message(TimeStampedModel, SoftDeletableModel):
    dialog = models.ForeignKey(models.JobApply, verbose_name=_("Dialog"), related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"), related_name="messages",
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("Message text"))
    read = models.BooleanField(verbose_name=_("Read"), default=False)
    all_objects = models.Manager()

    def get_formatted_create_datetime(self):
        return dj_date(localtime(self.created), settings.DATETIME_FORMAT)

    def __str__(self):
        return self.sender.username + "(" + self.get_formatted_create_datetime() + ") - '" + self.text + "'"
