from factory import django

from core.models import Task, TaskActivity
from users.models import User


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("id",)

    id: int = 1
    first_name = "Джон"
    last_name = "Андерсон"


class TaskFactory(django.DjangoModelFactory):
    class Meta:
        model = Task
        django_get_or_create = ("id",)


class TaskActivityFactory(django.DjangoModelFactory):
    class Meta:
        model = TaskActivity
        django_get_or_create = ("id",)
