from django.urls import path

from users.views import UsersWithTasksAPIView

urlpatterns = [
    path(
        'users-with-tasks/',
        UsersWithTasksAPIView.as_view(),
        name="users-with-tasks",
    )
]
