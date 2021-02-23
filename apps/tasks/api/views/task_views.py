from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.tasks.api.serializers.task_serializers import TaskSerializer

class TaskListAPIView(GeneralListApiView):
    serializer_class = TaskSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer


  
