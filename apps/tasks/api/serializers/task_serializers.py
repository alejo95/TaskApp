from rest_framework import serializers

from apps.tasks.models import Tasks
from apps.tasks.api.serializers.general_serializers import CategoryTaskSerializers
from apps.users.models import User

class TaskSerializer(serializers.ModelSerializer):
    category_task = serializers.StringRelatedField()
    user_task = serializers.StringRelatedField()

    class Meta:
        model = Tasks
        exclude = ('state','created_date','modified_date','deleted_date')


