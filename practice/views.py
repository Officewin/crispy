import random
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import Question, UserProgress


def get_random_questions(request):
    topics = request.GET.getlist('topic')
    qs = Question.objects.all()
    if topics:
        qs = qs.filter(skillset__topic__name__in=topics)
    questions = random.sample(list(qs), min(10, qs.count()))
    data = []
    for q in questions:
        data.append({
            'id': q.id,
            'type': q.type,
            'topic_name': q.skillset.topic.name,
            'skillset_name': q.skillset.name,
            'question_image': q.question_image.url if q.question_image else '',
            'option_a': q.option_a,
            'option_b': q.option_b,
            'option_c': q.option_c,
            'option_d': q.option_d,
        })
    return JsonResponse({'questions': data})


@require_POST
@login_required
def submit_answer(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return HttpResponseBadRequest('invalid question')

    answer = request.POST.get('answer')
    if answer is None:
        return HttpResponseBadRequest('answer required')

    progress, _ = UserProgress.objects.get_or_create(user=request.user, question=question)
    progress.attempts += 1
    correct = str(answer).strip().lower() == str(question.answer).strip().lower()
    if correct:
        progress.correct = True
    progress.save()
    return JsonResponse({'correct': correct, 'attempts': progress.attempts, 'skill_link': question.skill_link})
