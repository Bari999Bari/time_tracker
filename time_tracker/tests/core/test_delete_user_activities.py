import pytest
from rest_framework import status


@pytest.mark.django_db
def test_delete_user_activities_200(client, user,
                             task_activity_2,
                             get_delete_user_activities_url,
                             snapshot):
    client.force_authenticate(user)
    response = client.delete(get_delete_user_activities_url)
    assert response.status_code == status.HTTP_204_NO_CONTENT