from django.urls import path
from .views import (AllTodoView, CreateAPIView,
                    UpdateTodoView, DeleteTodoView,
                    )

urlpatterns = [
    path('all_todo/', AllTodoView.as_view()),
    path('create/', CreateAPIView.as_view()),
    path('update/', UpdateTodoView.as_view()),
    path('delete/', DeleteTodoView.as_view()),
]