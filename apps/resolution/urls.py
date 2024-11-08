from django.urls import include, path
from django.contrib.auth import get_user_model

from rest_framework import routers

from apps.resolution.models import Resolution, ResolutionConversation
from apps.resolution.views import (
    ResolutionViewSet,
    ResolutionConversationViewSet,
    CreateResolutionConversation,
)
from .views import ResolutionCategoryListView

User = get_user_model()

router = routers.DefaultRouter()

router.register(r"resolution", ResolutionViewSet, basename="resolution")

app_name = "resolution"

urlpatterns = [
    path("", include(router.urls), name="resolution"),
    path(
        "resolution-category/",
        ResolutionCategoryListView.as_view(),
        name="resolution-category",
    ),
    path(
        "resolution-conversation/<int:id>/",
        CreateResolutionConversation.as_view(),
        name="resolution-conversation",
    ),
]
