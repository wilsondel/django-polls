# Django
from django.urls import path

# Views
from . import views
from .views import IndexView, DetailQuestionView, ResultView

app_name = "polls"
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('detail/<int:pk>', DetailQuestionView.as_view(), name='detail'),
    path('results/<int:pk>', ResultView.as_view(), name='results'),
    path('vote/<int:question_id>', views.vote, name='vote')
]