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
    TicketSummaryComment
)
from apps.post_paid.serializers import TicketSummarySerializer, TicketSummaryCommentSerializer


User = get_user_model()


__all__ = ("TicketSummaryViewSet", "CreateTicketSummaryComment")


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


class CreateTicketSummaryComment(generics.CreateAPIView):
    serializer_class = TicketSummaryCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = TicketSummaryComment.objects.select_related(
        "ticket_summary", "user"
    ).all()

    def perform_create(self, serializer):
        user = self.request.user
        ticket_summary_id = self.kwargs.get("id")
        ticket_summary = get_object_or_404(
            TicketSummary, id=ticket_summary_id
        )
        comments = TicketSummaryComment.objects.select_related(
            "ticket_summary", "user"
        ).filter(ticket_summary=ticket_summary.id)
        if ticket_summary:
            emails = (
                ticket_summary.agent.user.email
                + " "
                + ticket_summary.company.client.user.email
            )
            emails = emails.split()

            # mail.send(
            #     "postmaster@psalmsglobal.com",
            #     bcc=emails,
            #     template="cust_interaction_comment_update",
            #     context={
            #         "interaction": ticket_summary,
            #         "comments": comments,
            #     },
            # )
        serializer.save(
            user=user, ticket_summary=ticket_summary
        )