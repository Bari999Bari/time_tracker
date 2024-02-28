import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from tests.factories import UserFactory, TaskFactory, TaskActivityFactory


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture
def task():
    return TaskFactory(id=201)


@pytest.fixture
def task_activity(user, task):
    return TaskActivityFactory(user=user, task=task, id=1)


@pytest.fixture
def get_start_task_activity_url():
    return reverse("start-activity")


@pytest.fixture
def start_activity_payload(task):
    return {
        "task": task.pk,
    }
