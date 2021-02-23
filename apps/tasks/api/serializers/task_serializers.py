from app.tasks.models import Task
from rest_framework import serializers
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclud = ('state','created_date','modified_date','deleted_date')
       

