from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.post_paid.models import InteractionRecord, TicketSummaryRecord
from apps.post_paid.serializers import (
    InteractionRecordSerializer,
    TicketSummaryInteractionRecordSerializer,
)

User = get_user_model()


__all__ = ("InteractionRecordViewSet", "TicketSummaryInteractionRecordViewSet")


class InteractionRecordViewSet(viewsets.ModelViewSet):
    serializer_class = InteractionRecordSerializer
    permisson_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["customer_interaction_post_paid__id"]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            qs = InteractionRecord.objects.select_related("client").filter(
                client__user__in=user
            ) or InteractionRecord.objects.select_related("agent").filter(
                agent__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = InteractionRecord.objects.all()
            return qs


class TicketSummaryInteractionRecordViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSummaryInteractionRecordSerializer
    permisson_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["ticket_summary__ticket_number"]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            qs = TicketSummaryRecord.objects.select_related("client").filter(
                client__user__in=user
            ) or TicketSummaryRecord.objects.select_related("agent").filter(
                agent__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = TicketSummaryRecord.objects.all()
            return qs
