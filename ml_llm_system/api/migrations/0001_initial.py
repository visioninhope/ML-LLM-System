# Generated by Django 4.2.2 on 2023-06-30 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtracurricularActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('grade_level', models.IntegerField(choices=[(9, '9'), (10, '10'), (11, '11'), (12, '12')])),
                ('attendance', models.IntegerField()),
                ('academic_performance_math', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('grade_math', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('academic_performance_english', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('grade_english', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('academic_performance_history', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('grade_history', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('academic_performance_science', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('grade_science', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('learning_preferences', models.CharField(choices=[('Visual', 'Visual'), ('Auditory', 'Auditory'), ('Kinesthetic', 'Kinesthetic')], max_length=12)),
                ('social_emotional_wellbeing', models.IntegerField()),
                ('recommendations', models.TextField(default='To be generated')),
                ('extracurricular_activities', models.ManyToManyField(to='api.extracurricularactivity')),
            ],
        ),
    ]
