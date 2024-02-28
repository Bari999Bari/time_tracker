from rest_framework import serializers

from core.models import TaskActivity


class CreateTaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = (
            'task',
        )


class TaskAgregatedByDurationSerializer(serializers.Serializer):
    task_name = serializers.CharField(source='task__name')
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        duration_seconds = obj.get('duration').seconds
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        return '{:02}:{:02}'.format(int(hours), int(minutes))
