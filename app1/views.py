from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
class AllTodoView(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class CreateTodoView(generics.CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    
class UpdateTodoView(generics.CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
class DeleteTodoView(generics.DestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    
# class TodaysTodo(views.APIView):
#     def get(self, request, *args, **kwargs):
#         today = date.today()
#         todos = TodoModel.objects.filter(created_at__date=today)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)

# class Last10DaysTodo(views.APIView):
#     def get(self, request, *args, **kwargs):
#         today = datetime.now()
#         last_ten = today -datetime.timedelta(days=10)
#         todos = TodoModel.objects.filter(created_ate_qte=last_ten, created_at_lte=today)
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data)