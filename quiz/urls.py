from django.urls import path
from .views import RandomQuestionView, SubmitAnswerView

urlpatterns = [
    path('questions/', RandomQuestionView.as_view(), name='random-questions'),
    path('submit/', SubmitAnswerView.as_view(), name='submit-answer'),
]
