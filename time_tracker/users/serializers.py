from rest_framework import serializers

from core.models import TaskActivity
from users.models import User


class ActivitySerializer(serializers.ModelSerializer):
    description = serializers.CharField(source="task.description")
    duration = serializers.DurationField()

    class Meta:
        model = TaskActivity
        fields = (
            'task',
            'description',
            'duration',
        )


class UsersWithTasksSerializer(serializers.ModelSerializer):
    tasks = ActivitySerializer(read_only=True, many=True, source='activities')

    class Meta:
        model = User
        fields = (
            'id',
            'fullname',
            'tasks'
        )
