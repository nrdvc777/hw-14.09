from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import ToDoModel
from .serializers import ToDoSerializer
from rest_framework.generics import *

class AllApiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)


class CreateApiView(CreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)


class UdateApiVIew(UpdateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)


class DeleteApiView(DestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)


class AllApiesApiView(RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated,)
