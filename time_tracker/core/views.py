from django.db import transaction
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.models import TaskActivity
from core.serializers import CreateTaskActivitySerializer


class StartTaskActivityView(generics.CreateAPIView):
    queryset = TaskActivity.objects.all()
    serializer_class = CreateTaskActivitySerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        user_ = request.user
        # Проверяем есть ли данная таска в работе у юзера
        if TaskActivity.objects.filter(user=user_, finished_at__isnull=True).exists():
            raise ValidationError(code=400, detail='Данная задача уже в работе')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = user_
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
