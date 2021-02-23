from apps.tasks.models import CategoryTask
from rest_framework import serializers

class CategoryTaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = CategoryTask
        exclude = ('state','created_date','modified_date','deleted_date')

