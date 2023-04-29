from post_office import mail

from django.contrib.auth import get_user, get_user_model

from rest_framework import generics, viewsets, permissions, filters
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client
from apps.callme.models import Company
from apps.post_paid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    TicketSummary,
)
from apps.post_paid.serializers import TicketSummarySerializer


User = get_user_model()


__all__ = ("TicketSummaryViewSet",)


class TicketSummaryViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSummarySerializer
    permisson_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "=ticket_number"
    ]
    lookup_field = "ticket_number"

    def get_queryset(self):
        current_user = self.request.user
        users = User.objects.filter(username=current_user)
        user = users.all()
        print(current_user)

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = TicketSummary.objects.select_related("company").filter(
                company__client__user__in=user
            )
            return qs
        elif current_user.designation_category == "staff":
            qs = TicketSummary.objects.all()
            return qs
        elif current_user.is_superuser:
            qs = TicketSummary.objects.filter(ticket_number__icontains="PSCI")
            return qs
