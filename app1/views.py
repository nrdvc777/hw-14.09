from django.shortcuts import render
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics

class AllTodoView(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class CreateTodoView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

# class DeleteToddoView(generics.RetrieveDestroyAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer

# class UpdateTodoView(generics.RetrieveUpdateAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer

class AllCreateDeleteUpdateTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
