from django.conf import settings
from django.db import models


class Question(models.Model):
    OPEN = 'open'
    MULTIPLE_CHOICE = 'multiple_choice'
    TYPE_CHOICES = [
        (OPEN, 'Open'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    topic_id = models.IntegerField()
    topic_name = models.CharField(max_length=100)
    skillset_id = models.IntegerField()
    skillset_name = models.CharField(max_length=100)
    question_image = models.ImageField(upload_to='questions/')
    answer = models.CharField(max_length=200)
    skill_link = models.URLField()

    option_a = models.CharField(max_length=200, blank=True, null=True)
    option_b = models.CharField(max_length=200, blank=True, null=True)
    option_c = models.CharField(max_length=200, blank=True, null=True)
    option_d = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.topic_name} - {self.skillset_name}"


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')
