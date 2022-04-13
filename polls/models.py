# Python 
import datetime

# Django
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    fk_question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text