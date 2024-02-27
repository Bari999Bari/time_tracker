from django.urls import path

from core.views import StartTaskActivityView, StopTaskActivityView

urlpatterns = [
    path(
        "start-activity/",
        StartTaskActivityView.as_view(),
        name="start-activity",
    ),
    path(
        "stop-activity/<int:id>/",
        StopTaskActivityView.as_view(),
        name="stop-activity",
    )
]
