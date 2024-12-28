from rest_framework import serializers
from .models import Task
from django.utils.timezone import now

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'due_date', 'created_at', 'updated_at', 'completed_at', 'user']

    def create(self, validated_data):
            # Automatically set the user to the authenticated user
            validated_data['user'] = self.context['request'].user
            return super().create(validated_data)
    

    def update(self, instance, validated_data):
        if instance.status == 'completed' and validated_data.get('status') != 'pending':
            raise serializers.ValidationError("Completed tasks cannot be edited unless reverted to pending.")
        
        if validated_data.get('status') == 'completed':
            validated_data['completed_at'] = now()
        elif validated_data.get('status') == 'pending':
            validated_data['completed_at'] = None

        return super().update(instance, validated_data)