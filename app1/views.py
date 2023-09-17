from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework.generics import *
from .models import ToDoModel
from .serializers import TodoSerializer

class AllTodoView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class CreateTodoView(CreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class UpdateTodoView(UpdateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class DeleteTodoView(DestroyAPIView):
    queryset =ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class AllofThemTodoView(RetrieveUpdateDestroyAPIView):
    queryset =ToDoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
