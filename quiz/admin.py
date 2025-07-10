from django.contrib import admin
from .models import Question, UserQuestion

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic_name', 'skillset_name', 'type')
    search_fields = ('topic_name', 'skillset_name')

@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'attempts', 'is_correct')
    search_fields = ('user__username', 'question__topic_name')
