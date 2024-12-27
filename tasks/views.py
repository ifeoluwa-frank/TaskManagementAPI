from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Fetch tasks only for the authenticated user
        return Task.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     # Automatically assign the task to the logged-in user
    #     serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
            # Fetch the task based on the id from the URL and ensure the authenticated user is the owner
            task = super().get_object()

            if task.user != self.request.user:
                raise PermissionDenied("You do not have permission to perform any operation this task.")
            
            return task


class AdminTaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]
    