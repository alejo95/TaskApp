from django.urls import path

from apps.tasks.api.views.general_views import CategoryTaskListAPIView
from apps.tasks.api.views.task_views import TaskListAPIView, TaskCreateAPIView

urlpatterns = [
    path('category_task/', CategoryTaskListAPIView.as_view(), name='category_task' ),
    path('list/', TaskListAPIView.as_view(), name='task_list' ),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
]  
