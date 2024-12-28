from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


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


class TaskUpdateStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """
        Handle status updates for a task: allow updates to `todo`, `in_progress`, or `completed`.
        """
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get("status")
        if new_status not in ["todo", "in_progress", "completed"]:
            return Response(
                {"detail": "Invalid status. Must be one of 'todo', 'in_progress', or 'completed'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Handle transitions to "completed"
        if new_status == "completed":
            if task.status == "completed":
                return Response(
                    {"detail": "Task is already marked as completed."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            task.status = "completed"
            task.completed_at = timezone.now()  # Set the timestamp for completion
            task.save()
            return Response(
                {
                    "detail": "Task marked as completed.",
                    "task": TaskSerializer(task).data,
                },
                status=status.HTTP_200_OK,
            )

        # Handle transitions from "completed" back to other statuses
        if task.status == "completed" and new_status in ["todo", "in_progress"]:
            task.status = new_status
            task.completed_at = None  # Clear the completion timestamp
            task.save()
            return Response(
                {
                    "detail": f"Task status updated to {new_status}.",
                    "task": TaskSerializer(task).data,
                },
                status=status.HTTP_200_OK,
            )

        # Handle updates to "todo" or "in_progress"
        if new_status in ["todo", "in_progress"]:
            task.status = new_status
            task.save()
            return Response(
                {
                    "detail": f"Task status updated to {new_status}.",
                    "task": TaskSerializer(task).data,
                },
                status=status.HTTP_200_OK,
            )

        return Response({"detail": "No changes made to the task."}, status=status.HTTP_400_BAD_REQUEST)


class TaskFilterView(ListAPIView):
    """
    List tasks with optional filtering by status, priority, and due_date.
    Supports sorting by due_date and priority.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'priority', 'due_date']  # Filters by fields
    ordering_fields = ['due_date', 'priority']  # Sorting options

    def get_queryset(self):
        # Ensure only tasks belonging to the authenticated user are returned
        return Task.objects.filter(user=self.request.user)