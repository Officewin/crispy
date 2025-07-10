from django.contrib import admin
from .models import Question, UserProgress, Topic, Skillset

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "skillset", "type")
    search_fields = ("skillset__name", "skillset__topic__name")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rank")
    ordering = ("rank",)


@admin.register(Skillset)
class SkillsetAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "name", "rank")
    list_filter = ("topic",)
    ordering = ("topic", "rank")

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "correct", "attempts", "answered_at")
    search_fields = ("user__username",)
