from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from profile_wizard import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()





'''

@receiver(post_save, sender=User)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
  if created:
      profile = models.FreeProfileWizard(user=instance)
      print(instance)
      profile.save()
'''