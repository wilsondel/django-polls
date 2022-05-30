# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

# CBV
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Models
from .models import Question, Choice

class IndexView(ListView):
    model = Question
    template_name = "polls/home.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailQuestionView(DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs["pk"]
        question = get_object_or_404(Question, pk=question_id)
        context['choices'] = question.choice_set.all()
        return context


class ResultView(DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs["pk"]
        question = get_object_or_404(Question, pk=question_id)
        context['choices'] = question.choice_set.all()
        return context

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
