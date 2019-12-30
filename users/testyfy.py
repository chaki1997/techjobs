

from django.test import TestCase
from profile_wizard import models

class AnimalTestCase(TestCase):
    def setUp(self):
         user = models.CustomUser
         qs = user.objects.get()
         print (qs)