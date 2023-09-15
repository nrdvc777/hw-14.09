from django.shortcuts import render

# Create your views here.
from .models import ToDoModel
from .serializers import ToDoSerializer
from rest_framework.generics import *

class AllApiView(ListAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

class CreateApiView(CreateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

class UdateApiVIew(UpdateAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

class DeleteApiView(DestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer

class AllApiesApiView(RetrieveUpdateDestroyAPIView):
    queryset = ToDoModel.objects.all()
    serializer_class = ToDoSerializer