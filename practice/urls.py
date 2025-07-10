from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('questions/', views.get_random_questions, name='questions'),
    path('answer/<int:pk>/', views.submit_answer, name='answer'),
]
