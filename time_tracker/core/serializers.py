from rest_framework import serializers

from core.models import TaskActivity


class CreateTaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = (
            'task',
        )


class TaskAggregatedByDurationSerializer(serializers.Serializer):
    task_name = serializers.CharField(source='task__name')
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        duration_seconds = obj.get('duration').seconds
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        return '{:02}:{:02}'.format(int(hours), int(minutes))


class ReadTaskActivitySerializer(serializers.ModelSerializer):
    started_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    finished_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = TaskActivity
        fields = (
            'task',
            'started_at',
            'finished_at',
        )


class AggregateUserActivitySerializer(serializers.Serializer):
    total_time = serializers.SerializerMethodField()

    def get_total_time(self, obj):
        if obj.get('total_time') is None:
            return '00:00'
        seconds = obj.get('total_time').seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return '{:02}:{:02}'.format(int(hours), int(minutes))
