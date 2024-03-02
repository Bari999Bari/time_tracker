from django.db.models import Prefetch, F, Sum, Window
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.models import TaskActivity
from users.models import User
from users.serializers import UsersWithTasksSerializer


class UsersWithTasksAPIView(generics.ListAPIView):
    """Получаем всех пользователей с информацией о затраченном времени
    на каждую конкретную задачу."""

    serializer_class = UsersWithTasksSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        prefetched = TaskActivity.objects.select_related('task', 'user').annotate(
            duration=Window(expression=Sum(F('finished_at') - F('started_at')), partition_by=[F('task'), F('user')])
        ).distinct('task', 'user')
        return User.objects.prefetch_related(Prefetch('activities', queryset=prefetched))
