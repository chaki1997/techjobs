from django.db import models
from django.conf import settings

# Create your models here.

class SubscriptionPlan(models.Model):

    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField()
    description = models.TextField()
    #image = models.ImageField(upload_to='products_images/', blank=True)
    billing_cycle = models.IntegerField(default=0)
    billing_cycle_unit = models.CharField(default='M',max_length=191)

    def __str__(self):
        return self.name

class Subscribtion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ID', on_delete=models.CASCADE,
                              null=True, blank=True)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user
