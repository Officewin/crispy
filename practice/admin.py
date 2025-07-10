from django.contrib import admin
from .models import Question, UserProgress

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "topic_name", "skillset_name", "type")
    search_fields = ("topic_name", "skillset_name")

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct", "attempts", "answered_at")
    search_fields = ("user__username",)
