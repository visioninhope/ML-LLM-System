# api/serializers.py

from rest_framework import serializers
from .models import Student, ExtracurricularActivity


class ExtracurricularActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularActivity
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    extracurricular_activities = ExtracurricularActivitySerializer(many=True)

    class Meta:
        model = Student
        fields = "__all__"
