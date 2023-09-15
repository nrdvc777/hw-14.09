from django.shortcuts import render
from .models import TodoModel
from rest_framework import views
from .serializers import TodoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from rest_framework.status import HTTP_204_NO_CONTENT
from datetime import date, datetime

class AllTodoView(views.APIView):
    def get(self, request):
        all_todos = TodoModel.objects.all()
        serializer = TodoSerializer(all_todos, many=True)
        return Response(serializer.data)

class DetailTodoView(views.APIView):
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id']) 
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
class CreateTodoView(views.APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UpdateTodoView(views.APIView):
    def patch(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id'])
        serializer = TodoSerializer(todo, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class DeleteTodoView(views.APIView):
    def delete(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoModel, id=kwargs['todo_id'])

        todo.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class TodaysTodo(views.APIView):
    def get(self, request, *args, **kwargs):
        today = date.today()
        todos = TodoModel.objects.filter(created_at__date=today)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

class Last10DaysTodo(views.APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.now()
        last_ten = today -datetime.timedelta(days=10)
        todos = TodoModel.objects.filter(created_ate_qte=last_ten, created_at_lte=today)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)