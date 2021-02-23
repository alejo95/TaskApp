from django.urls import path
from apps.tasks.api.views.general_views import CategoryTaskListAPIView

urlpatterns = [
    path('category_task/', CategoryTaskListAPIView.as_view(), name='category_task' ),
]
