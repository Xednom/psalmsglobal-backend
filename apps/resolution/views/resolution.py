from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets, permissions

from apps.core.models import ResolutionCategory
from apps.resolution.models import Resolution, ResolutionConversation
from apps.resolution.serializers import (
    ResolutionSerializer,
    ResolutionConversationSerializer,
    ResolutionCategorySerializer,
)


User = get_user_model()


__all__ = (
    "ResolutionViewSet",
    "ResolutionConversationViewSet",
    "ResolutionCategoryListView",
)


class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user = User.objects.filter(username=user)
        if user:
            return Resolution.objects.select_related(
                "category", "assigned_to", "client"
            ).filter(assigned_to__user__in=user) or Resolution.objects.select_related(
                "category", "assigned_to", "client"
            ).filter(
                client__user__in=user
            )


class ResolutionConversationViewSet(viewsets.ModelViewSet):
    queryset = ResolutionConversation.objects.select_related("resolution", "user").all()
    serializer_class = ResolutionConversationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResolutionCategoryListView(generics.ListAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer
