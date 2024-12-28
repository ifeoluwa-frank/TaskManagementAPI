from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TaskUpdateStatusView
from .views import AdminTaskListView, TaskFilterView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('admin/tasks/', AdminTaskListView.as_view(), name='admin-task-list'),
    path('tasks/<int:pk>/status/', TaskUpdateStatusView.as_view(), name='task-update-status'),
    path('tasks/filter/', TaskFilterView.as_view(), name='task-filter'),
    #path('tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]

