from django.urls import path
from .views import TaskListCreateView, TaskDetailView
from .views import AdminTaskListView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('admin/tasks/', AdminTaskListView.as_view(), name='admin-task-list'),
    #path('tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]

