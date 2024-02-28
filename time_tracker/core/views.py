import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import TaskActivity, Task
from core.serializers import CreateUpdateTaskActivitySerializer, TaskAggregatedByDurationSerializer, \
    ReadTaskActivitySerializer, AggregateUserActivitySerializer


class StartTaskActivityView(generics.CreateAPIView):
    """Начинает отчет времени по конкретной задаче."""

    queryset = TaskActivity.objects.all()
    serializer_class = CreateUpdateTaskActivitySerializer

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
    """Прекращает отчет времени по конкретной задаче."""

    queryset = Task.objects.all()
    serializer_class = CreateUpdateTaskActivitySerializer
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


class TaskAgregatedByDurationAPIView(generics.ListAPIView):
    """Показывает все трудозатраты пользователя за
    определенный промежуток времени, сгруппированные по задачам."""

    serializer_class = TaskAggregatedByDurationSerializer
    filter_backends = [DjangoFilterBackend]
    # фильтрация списка трудозатрат(пункт 5 типы запроса) будет
    # происходить только для завершенных активностей и которые
    # полностью попадают в период фильтрации
    filterset_fields = {
        'started_at': ['gte', 'lte'],
    }

    def get_queryset(self):
        # Выбираем только завершенные активности текущего пользователя
        # группируем по задачам и агрегируем продолжительность
        return (TaskActivity.objects
                .filter(user=self.request.user,
                        finished_at__isnull=False)
                .values('task__name')
                .annotate(duration=Sum(F('finished_at') - F('started_at')))
                .order_by('-duration'))


class TaskActivitiesAPIView(generics.ListAPIView):
    """Показывает все временные интервалы занятые работой
    для конкретного пользователя."""

    serializer_class = ReadTaskActivitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'started_at': ['gte', 'lte'],
    }

    def get_queryset(self):
        # Выбираем только активности текущего пользователя
        return (TaskActivity.objects
                .filter(user=self.request.user)
                .order_by('-started_at')
                )


class AggregateUserActivitiesAPIView(generics.RetrieveAPIView):
    """Показывает агрегированную сумму трудозатрат в часах
    для конкретного пользователя за определенный промежуток времени."""
    serializer_class = AggregateUserActivitySerializer

    def get_queryset(self):
        # Выбираем только активности текущего пользователя
        queryset = (TaskActivity.objects
                    .filter(user=self.request.user,
                            finished_at__isnull=False)

                    )
        return queryset

    def get_object(self):
        started_at__gte = self.request.query_params.get('started_at__gte')
        started_at__lte = self.request.query_params.get('started_at__lte')
        queryset = self.get_queryset()
        if started_at__gte is not None:
            queryset = queryset.filter(started_at__gte=started_at__gte)
        if started_at__lte is not None:
            queryset = queryset.filter(started_at__lte=started_at__lte)
        return queryset.aggregate(total_time=Sum(F('finished_at') - F('started_at')))


class AggregateAllActivitiesAPIView(AggregateUserActivitiesAPIView):
    """Показывает агрегированную сумму трудозатрат в часах
        для всех пользователей за определенный промежуток времени."""
    def get_queryset(self):
        return TaskActivity.objects.filter(finished_at__isnull=False)


class DeleteUseractivitiesAPIView(APIView):
    """Очищает данные трекинга конкретного пользователя."""
    def get_queryset(self):
        return TaskActivity.objects.filter(user=self.request.user)

    def delete(self, request):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
