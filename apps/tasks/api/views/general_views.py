from apps.base.api import GeneralListApiView
from apps.tasks.api.serializers.general_serializers import CategoryTaskSerializers

class CategoryTaskListAPIView(GeneralListApiView):
    serializer_class = CategoryTaskSerializers

