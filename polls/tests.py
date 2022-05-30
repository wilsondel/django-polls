# Python
import datetime
import time

# Django
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

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


# Auxiliar function
def create_question(question_text, days):
    """
    Create a question with the given question text and published the 
    given number of days offset to now.
    - Negative number for question published in the past
    - Positive number for question published in the future
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,pub_date=time)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """If no question exists, an appropiate message is displayed"""
        response = self.client.get(reverse('polls:home'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])


    def test_future_question(self):
        """
        Questions with a pub_date in future are not displayed on the index page
        """
        create_question(question_text="Future possible question",days=150)
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        create_question(question_text="Past question",days=-19)
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, "Past question")
        self.assertQuerysetEqual(response.context["latest_question_list"],Question.objects.all())

    def test_future_question_and_past_question(self):
        """
        Even if past and future question exists, only past question are displayed
        """
        past_question = create_question(question_text = 'Past question',days=-150)
        future_question = create_question(question_text = 'Future question',days=150)
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, "Past question")
        self.assertNotContains(response, "Future question")
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question])


    def test_two_past_questions(self):
        """
        The home page may display more than one question
        """
        past_question_1 = create_question(question_text = 'Past question 1',days=-102)
        past_question_2 = create_question(question_text = 'Past question 2',days=-202)
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, "Past question 1")
        self.assertContains(response, "Past question 2")
        self.assertQuerysetEqual(response.context["latest_question_list"], [past_question_1,past_question_2])

    def test_two_future_questions(self):
        """
        The home page should not display any question
        """
        future_question_1 = create_question(question_text = 'Future question 1',days=102)
        future_question_2 = create_question(question_text = 'Future question 2',days=202)
        response = self.client.get(reverse('polls:home'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

class QuestionDetailViewTests(TestCase):
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text
        """
        past_question = create_question(question_text = 'Past question 1',days=-102)
        url = reverse('polls:detail', args= (past_question.pk,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)