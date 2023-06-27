from django.db import models

class ExtracurricularActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    GRADES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    LEARNING_PREFERENCES = [
        ('Visual', 'Visual'),
        ('Auditory', 'Auditory'),
        ('Kinesthetic', 'Kinesthetic'),
    ]

    GRADE_LEVELS = [
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    ]

    name = models.CharField(max_length=100)
    grade_level = models.IntegerField(choices=GRADE_LEVELS)
    attendance = models.IntegerField()
    academic_performance_math = models.CharField(max_length=1, choices=GRADES)
    grade_math = models.CharField(max_length=1, choices=GRADES)
    academic_performance_english = models.CharField(max_length=1, choices=GRADES)
    grade_english = models.CharField(max_length=1, choices=GRADES)
    academic_performance_history = models.CharField(max_length=1, choices=GRADES)
    grade_history = models.CharField(max_length=1, choices=GRADES)
    academic_performance_science = models.CharField(max_length=1, choices=GRADES)
    grade_science = models.CharField(max_length=1, choices=GRADES)
    extracurricular_activities = models.ManyToManyField(ExtracurricularActivity)
    learning_preferences = models.CharField(max_length=12, choices=LEARNING_PREFERENCES)
    social_emotional_wellbeing = models.IntegerField()
    recommendations = models.TextField(default='To be generated')

    def __str__(self):
        return self.name
