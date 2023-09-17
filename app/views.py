from django.shortcuts import render
from.serializers import TodoSerializer
from.models import ToDoModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class AllTodoView(generics.ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class RetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer

