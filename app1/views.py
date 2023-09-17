from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from rest_framework import generics
from rest_framework.generics import *
from .models import TodoModel
from .serializers import TodoSerializer

class AllTodoView(ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class CreateTodoView(CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class UpdateTodoView(UpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class DeleteTodoView(DestroyAPIView):
    queryset =TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class AllofThemTodoView(RetrieveUpdateDestroyAPIView):
    queryset =TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
