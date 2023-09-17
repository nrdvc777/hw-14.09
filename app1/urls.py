from django.urls import path
from .views import (AllTodoView, 
                    CreateTodoView, UpdateTodoView, 
                    DeleteTodoView, )

urlpatterns = [
    path('all_todo/', AllTodoView.as_view()),
    path('create/', CreateTodoView.as_view()),
    path('update/<int:todo_id>/', UpdateTodoView.as_view()),
    path('delete/<int:todo_id>/', DeleteTodoView.as_view()),
]