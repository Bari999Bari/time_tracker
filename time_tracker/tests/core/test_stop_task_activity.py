import pytest
from rest_framework import status


@pytest.mark.django_db
def test_stop_task_activity_200(client, user, task, task_activity, get_stop_task_activity_url, stop_activity_payload):
    client.force_authenticate(user)
    response = client.put(get_stop_task_activity_url, data=stop_activity_payload)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_stop_task_activity_401(client, get_stop_task_activity_url, stop_activity_payload, snapshot):
    response = client.put(get_stop_task_activity_url, data=stop_activity_payload)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    snapshot.assert_match(response.json())


@pytest.mark.django_db
def test_stop_task_activity_400(client, user, get_stop_task_activity_url, stop_activity_payload,
                                 snapshot):
    client.force_authenticate(user)
    response = client.put(get_stop_task_activity_url, data=stop_activity_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    snapshot.assert_match(response.json())