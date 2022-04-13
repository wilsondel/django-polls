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

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns true for questions whose pub_date is in the current time"""
        time = timezone.now()
        present_questions = Question(question_text="Who is the teacher at platzi?",pub_date=time)
        self.assertEquals(present_questions.was_published_recently(), True)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns false for questions whose pub_date is in the past"""
        time = timezone.now() - datetime.timedelta(days=2)
        present_questions = Question(question_text="Who is the teacher at platzi?",pub_date=time)
        self.assertEquals(present_questions.was_published_recently(), False)
