from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAdminUser]
    def get_permissions(self):
        # Allow only admin users to list all users
        if self.request.method == "GET":
            return [permissions.IsAdminUser()]
        # Allow anyone to create a user
        elif self.request.method == "POST":
            return [permissions.AllowAny()]
        return super().get_permissions()


# class IsAdminOrSelf(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Allow admin or the user accessing their own data
#         return request.user.is_staff or obj == request.user


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure users can only access their own details
        user = self.request.user
        if not user.is_staff:
            return User.objects.filter(id=user.id)
        return super().get_queryset()
