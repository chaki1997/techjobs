from django.test import TestCase
from django.urls import reverse

from .models import FreeProfileWizard


class PostTests(TestCase):
    models_class = FreeProfileWizard
    def setUp(self):
        profile = self.models_class


