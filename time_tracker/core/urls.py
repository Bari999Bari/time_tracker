from django.urls import path

from core.views import StartTaskActivityView, StopTaskActivityView, TaskAgregatedByDurationAPIView

urlpatterns = [
    path(
        'start-activity/',
        StartTaskActivityView.as_view(),
        name="start-activity",
    ),
    path(
        'stop-activity/<int:id>/',
        StopTaskActivityView.as_view(),
        name="stop-activity",
    ),
    path('labour-costs/',
         TaskAgregatedByDurationAPIView.as_view(),
         name="labour-costs"),
]
