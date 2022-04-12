# Python
import datetime

# Django
from django.test import TestCase
from django.utils import timezone
from .models import Question
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns false for questions whose pub_date is in future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_questions = Question(question_text="Who is the best course director at platzi?",pub_date=time)
        self.assertEquals(future_questions.was_published_recently(), False)
