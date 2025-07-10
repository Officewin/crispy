from django.db import models
from django.conf import settings

class Question(models.Model):
    OPEN = "open"
    MULTIPLE_CHOICE = "multiple_choice"
    QUESTION_TYPES = [
        (OPEN, "Open"),
        (MULTIPLE_CHOICE, "Multiple Choice"),
    ]
    type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    topic_id = models.IntegerField()
    topic_name = models.CharField(max_length=200)
    skillset_id = models.IntegerField()
    skillset_name = models.CharField(max_length=200)
    question_image = models.ImageField(upload_to="questions/", blank=True, null=True)
    answer = models.CharField(max_length=100)
    skill_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.topic_name} - {self.skillset_name}"

class UserQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user} - {self.question}"
