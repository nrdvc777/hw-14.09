from django.urls import path
from .views import (AllTodoView, AllCreateDeleteUpdateTodoView, CreateTodoView)

urlpatterns = [
    path('all_todo/', AllTodoView.as_view()),
    path('create/', CreateTodoView.as_view()),
    path('<int:pk>', AllCreateDeleteUpdateTodoView.as_view()),
]
