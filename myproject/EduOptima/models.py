from django.db import models

# Create your models here.

# MODEL 1 - STUDENT LEARNING ENVIRONMENT

from django.db import models

class Classroom(models.Model):
    """Model representing a classroom."""
    name = models.CharField(max_length=100, blank=False, null=False)
    grade_level = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    """Model representing a teacher."""
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    classrooms = models.ManyToManyField(Classroom, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    """Model representing a student."""
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ... continue for other models ...

class Attendance(models.Model):
    """Model representing a student's attendance on a particular day."""
    ATTENDANCE_STATUS = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LATE', 'Late'),
    ]

    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ATTENDANCE_STATUS, default='PRESENT')

    def __str__(self):
        return f"{self.student} - {self.date}"

# ... continue for other models ...

class Grade(models.Model):
    """Model representing a student's grade for a particular assignment."""
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)])

    def __str__(self):
        return f"{self.student} - {self.assignment}"
# ... continue for other models ...
