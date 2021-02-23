from apps.base.api import GeneralListApiView
from apps.tasks.api.serializers.task_serializers import TaskSerializer

class TaskListAPIView(GeneralListApiView):
    serializer_class = TaskSerializer
 


  
