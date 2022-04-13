from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

def home(request):
    q = Question.objects.all()
    return render(request,"polls/home.html",{"latest_question_list":q})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request,"polls/detail.html",{"question": question,"choices":choices})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request,"polls/results.html",{"question": question, "choices":choices})

def vote(request, question_id):
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question,pk=question_id)
    choices = question.choice_set.all()
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        print("Selected choice: ", selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # print("This is the Question: ",Question)
        return render(request,"polls/detail.html",
        {
            "question": question,
            "choices": choices,
            "error_message": "You did not make a choice. Please, select one option."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
