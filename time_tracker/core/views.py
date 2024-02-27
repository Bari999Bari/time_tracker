import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.models import TaskActivity, Task
from core.serializers import CreateTaskActivitySerializer


class StartTaskActivityView(generics.CreateAPIView):
    queryset = TaskActivity.objects.all()
    serializer_class = CreateTaskActivitySerializer

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


class StopTaskActivityView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskActivitySerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        try:
            task_activity = TaskActivity.objects.get(user=request.user,
                                                     task=task,
                                                     finished_at__isnull=True
                                                     )
            task_activity.finished_at = datetime.datetime.now()
            task_activity.save()
        except ObjectDoesNotExist:
            raise ValidationError(code=400, detail='Задача не взята в работу')
        return Response(status=status.HTTP_200_OK)
