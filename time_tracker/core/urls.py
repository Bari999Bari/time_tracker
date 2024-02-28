from django.urls import path

from core.views import (StartTaskActivityView, StopTaskActivityView, TaskAggregatedByDurationAPIView,
                        TaskActivitiesAPIView, AggregateUserActivitiesAPIView, AggregateAllActivitiesAPIView,
                        DeleteUseractivitiesAPIView,
                        )

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
         TaskAggregatedByDurationAPIView.as_view(),
         name="labour-costs"),
    path('task-activities/',
         TaskActivitiesAPIView.as_view(),
         name="task-activities"),
    path('aggregate-user-activities/',
         AggregateUserActivitiesAPIView.as_view(),
         name="aggregate-user-activities"),
    path('aggregate-all-activities/',
         AggregateAllActivitiesAPIView.as_view(),
         name="aggregate-all-activities"),
    path('remove-user-activities/',
         DeleteUseractivitiesAPIView.as_view(),
         name="remove-user-activities"),
]
