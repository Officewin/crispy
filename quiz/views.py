from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Question, UserQuestion
from .serializers import QuestionSerializer

class RandomQuestionView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        topics = self.request.query_params.get('topic')
        queryset = Question.objects.all()
        if topics:
            topic_ids = [int(t) for t in topics.split(',') if t.isdigit()]
            queryset = queryset.filter(topic_id__in=topic_ids)
        return queryset.order_by('?')[:10]

class SubmitAnswerView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        answer = str(request.data.get('answer', '')).strip()
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            return Response({'detail': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        user_question, _ = UserQuestion.objects.get_or_create(user=request.user, question=question)
        if user_question.is_correct:
            return Response({'detail': 'Question already answered correctly'}, status=200)
        user_question.attempts += 1
        if question.answer.strip().lower() == answer.lower():
            user_question.is_correct = True
            user_question.save()
            return Response({'correct': True})
        user_question.save()
        data = {
            'correct': False,
            'attempts': user_question.attempts,
            'skill_link': question.skill_link,
        }
        return Response(data)
