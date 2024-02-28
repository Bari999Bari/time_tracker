import datetime

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
    return TaskFactory(id=201, name='first')


@pytest.fixture
def task_activity(user, task):
    return TaskActivityFactory(user=user, task=task, id=1)


@pytest.fixture
def task_activity_2(user, task):
    return TaskActivityFactory(user=user, task=task, id=1,
                               started_at=datetime.datetime(2024, 2, 23, 10, 30, 20),
                               finished_at=datetime.datetime(2024, 2, 23, 12, 30, 20), )



@pytest.fixture
def get_start_task_activity_url():
    return reverse("start-activity")


@pytest.fixture
def get_stop_task_activity_url(task):
    return reverse("stop-activity", kwargs={'id': task.pk})


@pytest.fixture
def get_task_aggregate_by_duration_url(task):
    return reverse("labour-costs")


@pytest.fixture
def start_activity_payload(task):
    return {
        "task": task.pk,
    }


@pytest.fixture
def stop_activity_payload(task):
    return {
        "task": task.pk,
    }
