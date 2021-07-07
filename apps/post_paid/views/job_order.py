from django.contrib.auth import get_user_model
from apps.post_paid import serializers

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client, Staff
from apps.post_paid.models import JobOrderPostPaid, CustomerInteractionPostPaid
from apps.post_paid.serializers import JobOrderPostPaidSerializer

User = get_user_model()


__all__ = ("JobOrderPostPaidViewSet",)


class JobOrderPostPaidViewSet(viewsets.ModelViewSet):
    queryset = JobOrderPostPaid.objects.select_related(
        "client", "caller_interaction_record"
    ).all()
    serializer_class = JobOrderPostPaidSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["caller_interaction_record__ticket_number"]
