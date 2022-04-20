# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# CBV
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Models
from .models import Question, Choice

# def home(request):
#     q = Question.objects.all()
#     return render(request,"polls/home.html",{"latest_question_list":q})

class IndexView(ListView):
    model = Question
    template_name = "polls/home.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request,"polls/detail.html",{"question": question,"choices":choices})

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = context['id'].choice_set.all()
        return context


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
