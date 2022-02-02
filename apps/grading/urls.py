from django.urls import path, include
from rest_framework import routers

from apps.grading.views import (
    PostpaidInteractionRatingView,
    PrepaidInteractionRatingView,
)

app_name = "grading"

urlpatterns = [
    path(
        "postpaid/<int:id>/rate/",
        PostpaidInteractionRatingView.as_view(),
        name="postpaid",
    ),
    path(
        "prepaid/<int:id>/rate/", PrepaidInteractionRatingView.as_view(), name="prepaid"
    ),
]
