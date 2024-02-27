from django.urls import path

from core.views import StartTaskActivityView

urlpatterns = [
    path(
        "start-activity/",
        StartTaskActivityView.as_view(),
        name="start-activity",
    )
]