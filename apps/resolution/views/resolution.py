from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions

from apps.resolution.models import Resolution, ResolutionConversation
from apps.resolution.serializers import (
    ResolutionSerializer,
    ResolutionConversationSerializer,
)


User = get_user_model()


__all__ = ("ResolutionViewSet", "ResolutionConversationViewSet")


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
