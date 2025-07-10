from django.conf import settings
from django.db import models


class Topic(models.Model):
    """A SAT math topic such as Algebra or Geometry."""

    name = models.CharField(max_length=100, unique=True)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["rank", "name"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return self.name


class Skillset(models.Model):
    """A skillset belonging to a specific topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="skillsets")
    name = models.CharField(max_length=100)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("topic", "name")
        ordering = ["topic__rank", "rank", "name"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.topic.name} - {self.name}"


class Question(models.Model):
    OPEN = "open"
    MULTIPLE_CHOICE = "multiple_choice"
    TYPE_CHOICES = [
        (OPEN, "Open"),
        (MULTIPLE_CHOICE, "Multiple Choice"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    skillset = models.ForeignKey(Skillset, on_delete=models.CASCADE)
    question_image = models.ImageField(upload_to="questions/")
    answer = models.CharField(max_length=200)
    skill_link = models.URLField()

    option_a = models.CharField(max_length=200, blank=True, null=True)
    option_b = models.CharField(max_length=200, blank=True, null=True)
    option_c = models.CharField(max_length=200, blank=True, null=True)
    option_d = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.skillset.topic.name} - {self.skillset.name}"


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')
