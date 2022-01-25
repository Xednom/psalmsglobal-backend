from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions

from apps.resolution.models import Resolution, ResolutionConversation
from apps.resolution.serializers import (
    ResolutionSerializer,
    ResolutionConversationSerializer,
)


User = get_user_model()


class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user = User.objects.get(username=user)
        if user:
            return Resolution.objects.select_related(
                "category", "assigned_to", "client"
            ).filter(assigned_to__user__in=user) or Resolution.objects.select_related(
                "category", "assigned_to", "client"
            ).filter(
                client__user__in=user
            )
