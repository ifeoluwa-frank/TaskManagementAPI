from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskListCreateView(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    # serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access
    permission_classes = [IsAuthenticated]  # Protect the view

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)  # Fetch tasks for the authenticated user
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Automatically assign the task to the logged-in user
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
