from django.db import models
from django.conf import settings
from profile_wizard import models as jobmodel
# Create your models here.

class JobApply(models.Model):
    applier = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='applier',  on_delete=models.CASCADE,
                              null=True, blank=True)
    applier_profile = models.ForeignKey(jobmodel.EmployeeProfileModel,related_name='job',  on_delete=models.CASCADE,
                                 null=True, blank=True)
    jobowner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='jobowner',  on_delete=models.CASCADE,
                              null=True, blank=True)
    job = models.ForeignKey(jobmodel.PostJob,related_name='job',  on_delete=models.CASCADE,
                                 null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    coverletter = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return u'{0} ({1})'.format(self.job,self.applier)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.job,self.applier)


class Contract(models.Model):
    status = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    job_signed = models.ForeignKey(jobmodel.PostJob, related_name='job_signed', on_delete=models.CASCADE,
                            null=True, blank=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employee', on_delete=models.CASCADE,
                                null=True, blank=True)

    employer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employer', on_delete=models.CASCADE,
                                 null=True, blank=True)
    jobapply = models.ForeignKey(JobApply, related_name='jobapply', on_delete=models.CASCADE,
                            null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return u'{0} ({1})'.format(self.job_signed,self.jobapply)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.job_signed,self.jobapply)
