from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import users_serializer


class UsersWithTasksAPIView(APIView):
    """Получаем всех пользователей с информацией о затраченном времени
    на каждую конкретную задачу."""

    def get(self, request):
        queryset = User.objects.prefetch_related('activities').all()
        data = users_serializer(queryset)
        return Response(data=data, status=status.HTTP_200_OK)
