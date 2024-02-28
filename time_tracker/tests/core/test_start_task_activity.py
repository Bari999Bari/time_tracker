import pytest
from rest_framework import status


@pytest.mark.django_db
def test_start_task_activity_201(client, user, get_start_task_activity_url, start_activity_payload):
    client.force_authenticate(user)
    response = client.post(get_start_task_activity_url, data=start_activity_payload)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_start_task_activity_401(client, get_start_task_activity_url, start_activity_payload, snapshot):
    response = client.post(get_start_task_activity_url, data=start_activity_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    snapshot.assert_match(response.json())


@pytest.mark.django_db
def test_start_task_activity_400(client, user, task_activity, get_start_task_activity_url, start_activity_payload,
                                 snapshot):
    client.force_authenticate(user)
    response = client.post(get_start_task_activity_url, data=start_activity_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    snapshot.assert_match(response.json())
