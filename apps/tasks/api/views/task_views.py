from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.tasks.api.serializers.task_serializers import TaskSerializer

class TaskListAPIView(GeneralListApiView):
    serializer_class = TaskSerializer


class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tarea creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)






















