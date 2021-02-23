from django.urls import path

from apps.tasks.api.views.general_views import CategoryTaskListAPIView
from apps.tasks.api.views.task_views import TaskListAPIView, TaskCreateAPIView, TaskRetrieveAPIView, TaskDestroyAPIView

urlpatterns = [
    path('category_task/', CategoryTaskListAPIView.as_view(), name='category_task' ),
    path('list/', TaskListAPIView.as_view(), name='task_list' ),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('task/detail/<int:pk>', TaskRetrieveAPIView.as_view(), name='task_detail'),
    path('task/destroy/<int:pk>', TaskDestroyAPIView.as_view(), name='task_desroy'),
]  
