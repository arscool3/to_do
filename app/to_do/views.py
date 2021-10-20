
from rest_framework import generics
from .serializers import TaskDetailSerializer, TaskListSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from .models import Task
from .permissions import IsOwnerOrReadyOnly, IsEmployee
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User

from .tasks import send_email_task
from rest_framework_simplejwt.views import TokenObtainPairView


for task in Task.objects.all():
    for user in User.objects.all():
        if task.user == user:
            send_email_task(user)


class TaskCreatView(generics.CreateAPIView) :

    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    #permission_classes = (IsAuthenticated, )
    permission_classes = (IsEmployee, )

class TaskListView(generics.ListAPIView) :


    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, )
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView) :
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwnerOrReadyOnly, )

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView) :
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer