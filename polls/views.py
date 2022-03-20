from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question

def home(request):
    q = Question.objects.all()
    return render(request,"polls/home.html",{"latest_question_list":q})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request,"polls/detail.html",{"question": question,"choices":choices})


def results(request, question_id):
    return HttpResponse(f"These are the results for question number: {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You are voting for question number: {question_id}")
