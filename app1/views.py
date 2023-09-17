from django.shortcuts import render
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
class AllTodoView(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


class CreateTodoView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


# class DeleteToddoView(generics.RetrieveDestroyAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer

# class UpdateTodoView(generics.RetrieveUpdateAPIView):
#     queryset = TodoModel.objects.all()
#     serializer_class = TodoSerializer

class AllCreateDeleteUpdateTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
