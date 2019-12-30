import datetime

from django.test import TestCase
from django.utils import timezone

from .models import CustomUser


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        #time = timezone.now() + datetime.timedelta(days=30)
        #future_question = CustomUser.save(self,username='gio')
        #self.assertIs(future_question.was_published_recently(), False)