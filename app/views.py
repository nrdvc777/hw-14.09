from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.generics import *
from .models import TodoModel
from .serializers import TodoSerializer

class AllTodoView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class CreateTodoView(CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoView(UpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoView(DestroyAPIView):
    queryset =TodoModel.objects.all()
    serializer_class = TodoSerializer

class AllofThemTodoView(RetrieveUpdateDestroyAPIView):
    queryset =TodoModel.objects.all()
    serializer_class = TodoSerializer