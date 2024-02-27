from rest_framework import serializers

from core.models import TaskActivity


class CreateTaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = (
            'task',
        )
