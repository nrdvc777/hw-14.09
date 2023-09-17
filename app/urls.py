from django.urls import path
from .views import (AllTodoView, RetriveUpdateDestroyView)

urlpatterns = [
    path('all/', AllTodoView.as_view()),
    path('rud/', RetriveUpdateDestroyView.as_view()),
]