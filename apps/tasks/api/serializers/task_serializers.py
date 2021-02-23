from rest_framework import serializers

from apps.tasks.models import Tasks
from apps.tasks.api.serializers.general_serializers import CategoryTaskSerializers

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        exclude = ('state','created_date','modified_date','deleted_date')

