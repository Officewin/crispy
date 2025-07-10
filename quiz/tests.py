from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Question

User = get_user_model()

class QuizAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass')
        for i in range(15):
            Question.objects.create(
                type=Question.OPEN,
                topic_id=1,
                topic_name='Algebra',
                skillset_id=1,
                skillset_name='Linear',
                answer='42'
            )

    def test_fetch_random_questions(self):
        self.client.login(username='test', password='pass')
        url = reverse('random-questions')
        response = self.client.get(url + '?topic=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
