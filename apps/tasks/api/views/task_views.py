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
 


class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    
    def delete(self, request,pk = None):
        task = self.get_queryset().filter(id = pk).first()
        if task:
            task.state = False
            task.save()
            return Response({'message:': 'Tarea eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error:': 'No existe tarea con esos datos'}, status = status.HTTP_400_BAD_REQUEST)
 

class taskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self,pk):
         return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self, request, pk= None):
        task = self.get_queryset(pk)
        if task:
            task_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(task_serializer.data,status = status.HTTP_200_OK)
        return Response({'error:': 'No existe tarea con esos datos'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        if self.get_queryset(pk):
            Task_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if Task_serializer.is_valid():
                Task_serializer.save()
                return Response(Task_serializer.data,status = status.HTTP_200_OK)
            return Response(Task_serializer.error,status = status.HTTP_400_BAD_REQUEST)


 











