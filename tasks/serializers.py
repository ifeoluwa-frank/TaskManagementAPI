from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user']

    def create(self, validated_data):
            # Automatically set the user to the authenticated user
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)