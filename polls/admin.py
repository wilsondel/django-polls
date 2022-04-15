# Django
from django.contrib import admin

# Models
from polls.models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text","pub_date","mod_date","was_published_recently")
    list_filter = ["pub_date","mod_date"]
    search_fields = ["question_text"]


# admin.site.register(Question, QuestionAdmin) => @admin.register(Question)
