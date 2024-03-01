from django.db.models import QuerySet, Sum, F
from rest_framework import serializers

from core.models import TaskActivity
from users.models import User


def users_serializer(queryset: QuerySet) -> dict:
    users = [single_user_serialize(user_) for user_ in queryset]
    return {'count': queryset.count(),
            'users': users}


def single_user_serialize(user: User) -> dict:
    return {'id': user.pk,
            'fullname': '{} {}'.format(user.first_name, user.last_name),
            'tasks': get_user_tasks_labour_costs(user)}


def get_user_tasks_labour_costs(user: User) -> list:
    task_activities_queryset = (user.activities
                                .filter(finished_at__isnull=False)
                                .values('task__name', 'task__description')
                                .annotate(duration=Sum(F('finished_at') - F('started_at')))
                                .order_by('-duration'))
    serializer = UserTasksLabourCostsSerializer(task_activities_queryset, many=True)
    serializer_return_list = serializer.data

    converted_data = []
    for ordered_dict in serializer_return_list:
        converted_data.append(dict(ordered_dict))

    return converted_data


class UserTasksLabourCostsSerializer(serializers.Serializer):
    name = serializers.CharField(source='task__name')
    description = serializers.CharField(source='task__name')
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        duration_seconds = obj.get('duration').seconds
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        return '{:02}:{:02}'.format(int(hours), int(minutes))
