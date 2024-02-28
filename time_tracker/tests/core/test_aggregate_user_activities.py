import pytest
from rest_framework import status


@pytest.mark.django_db
def test_aggregate_user_activities_200(client, user,
                             task_activity_2,
                             get_aggregate_user_activities_url,
                             snapshot):
    client.force_authenticate(user)
    response = client.get(get_aggregate_user_activities_url)
    assert response.status_code == status.HTTP_200_OK
    snapshot.assert_match(response.json())