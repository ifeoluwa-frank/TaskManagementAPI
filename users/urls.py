from django.urls import path
from .views import UserListCreateView, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    #path('api/login/', obtain_auth_token, name='api-login'),
]
