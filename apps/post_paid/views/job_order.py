from django.contrib.auth import get_user_model
from apps.post_paid import serializers

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client, Staff
from apps.post_paid.models import JobOrderPostPaid, CustomerInteractionPostPaid
from apps.post_paid.serializers import JobOrderPostPaidSerializer

User = get_user_model()


__all__ = ("JobOrderPostPaidViewSet", "JobOrderViewSet")


class JobOrderPostPaidViewSet(viewsets.ModelViewSet):
    queryset = JobOrderPostPaid.objects.select_related(
        "client", "caller_interaction_record"
    ).all()
    serializer_class = JobOrderPostPaidSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["caller_interaction_record__ticket_number"]


class JobOrderViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderPostPaidSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        current_user = self.request.user
        clients = User.objects.filter(username=current_user)
        staffs = User.objects.filter(username=current_user)
        client = clients.all()
        staff = staffs.all()

        if current_user:
            queryset = JobOrderPostPaid.objects.select_related(
                "client"
            ).filter(client__user__in=client) or JobOrderPostPaid.objects.select_related(
                "client").filter(
                va_assigned__user__in=staff
            )
            return queryset
        else:
            queryset = JobOrderPostPaid.objects.all()
            return queryset