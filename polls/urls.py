# Django
from django.urls import path

# Views
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.home, name='home'),
    path('thething/<int:question_id>', views.detail, name='detail'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote')
]