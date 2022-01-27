from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets, permissions
from rest_framework.generics import get_object_or_404

from apps.core.models import ResolutionCategory
from apps.resolution.models import Resolution, ResolutionConversation, resolution
from apps.resolution.serializers import (
    ResolutionSerializer,
    ResolutionConversationSerializer,
    ResolutionCategorySerializer,
)


User = get_user_model()


__all__ = (
    "ResolutionViewSet",
    "ResolutionConversationViewSet",
    "CreateResolutionConversation",
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


class CreateResolutionConversation(generics.CreateAPIView):
    serializer_class = ResolutionConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        resolution_id = self.kwargs.get("id")
        resolution = get_object_or_404(Resolution, id=resolution_id)
        serializer.save(user=user, resolution=resolution)


class ResolutionCategoryListView(generics.ListAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer
