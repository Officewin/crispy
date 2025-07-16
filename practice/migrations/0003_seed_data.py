from django.db import migrations

def seed_data(apps, schema_editor):
    Topic = apps.get_model('practice', 'Topic')
    Skillset = apps.get_model('practice', 'Skillset')

    topics = [
        (1, 'Algebra'),
        (2, 'Advanced Math'),
        (3, 'Problem Solving and Data Analysis'),
        (4, 'Geometry and Trigonometry'),
    ]

    skillsets = [
        (1, 1, 'Linear equations'),
        (2, 1, 'System of equations'),
        (3, 2, 'Quadratics'),
        (4, 2, 'Exponents'),
        (5, 3, 'Data interpretation'),
        (6, 4, 'Angles'),
    ]

    for topic_id, name in topics:
        Topic.objects.get_or_create(topic_id=topic_id, defaults={'name': name, 'rank': topic_id})

    for skillset_id, topic_id, name in skillsets:
        topic = Topic.objects.get(topic_id=topic_id)
        Skillset.objects.get_or_create(skillset_id=skillset_id, topic=topic, defaults={'name': name, 'rank': skillset_id})

def unseed_data(apps, schema_editor):
    Topic = apps.get_model('practice', 'Topic')
    Skillset = apps.get_model('practice', 'Skillset')

    Skillset.objects.filter(skillset_id__in=[1,2,3,4,5,6]).delete()
    Topic.objects.filter(topic_id__in=[1,2,3,4]).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_add_ids'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
