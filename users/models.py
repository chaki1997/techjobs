
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from. choices import STATUS
# Create your models here.


class CustomUser(AbstractUser):

    # add additional fields in here
    is_employer = models.BooleanField(default=False)
    is_jobseeker = models.BooleanField(default=False)
    status = models.CharField(max_length=64, blank=False,default='empty')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('customuser')
        verbose_name_plural = _('customusers')
        #abstract = True
        ordering = ('id','is_employer','is_jobseeker' )

    def __str__(self):
        return self.username

    def __unicode__(self):
        return u'{0} ({1})'.format(self.get_full_name(), self.email)