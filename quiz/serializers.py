from rest_framework import serializers
from .models import Question, UserQuestion

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id', 'type', 'topic_id', 'topic_name',
            'skillset_id', 'skillset_name', 'question_image',
            'answer', 'skill_link'
        ]
        read_only_fields = ['id']

class UserQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = UserQuestion
        fields = ['id', 'user', 'question', 'attempts', 'is_correct']
        read_only_fields = ['id', 'user', 'question']
