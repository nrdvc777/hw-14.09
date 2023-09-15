from django.urls import path
from .views import (CreateAPIView,AllApiView,AllApiesApiView,UdateApiVIew,DeleteApiView)
urlpatterns = [
    path('todos', AllApiView.as_view()),
    path('create/', CreateAPIView.as_view()),
    path('update/', UdateApiVIew.as_view()),
    path('delete/', DeleteApiView.as_view()),
    path('<int:pk>/', AllApiesApiView.as_view()),
]