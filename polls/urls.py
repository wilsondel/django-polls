# Django
from django.urls import path

# Views
from . import views
from .views import IndexView

app_name = "polls"
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('results/<int:question_id>', views.results, name='results'),
    path('vote/<int:question_id>', views.vote, name='vote')
]