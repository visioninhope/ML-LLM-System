from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Student, ExtracurricularActivity
from .serializers import StudentSerializer, ExtracurricularActivitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ExtracurricularActivityViewSet(viewsets.ModelViewSet):
    queryset = ExtracurricularActivity.objects.all()
    serializer_class = ExtracurricularActivitySerializer
