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
    CustomerInteractionPostPaid,
    CustomerInteractionPostPaidComment,
)
from apps.post_paid.serializers import (
    InterestedToSellSerializer,
    InterestedToBuySerializer,
    GeneralCallSerializer,
    CustomerInteractionPostPaidCommentSerializer,
    CustomerInteractionPostPaidSerializer,
)

User = get_user_model()


__all__ = (
    "InterestedToBuyViewSet",
    "InterestedToSellViewSet",
    "GeneralCallViewSet",
    "CustomerInteractionPostPaidViewSet",
    "CreateCustomerInteractionPostPaidComment",
)


class InterestedToBuyViewSet(viewsets.ModelViewSet):
    serializer_class = InterestedToBuySerializer
    permisson_classes = [permissions.IsAuthenticated]
    queryset = InterestedToBuy.objects.all()


class InterestedToSellViewSet(viewsets.ModelViewSet):
    serializer_class = InterestedToSellSerializer
    permisson_classes = [permissions.IsAuthenticated]
    queryset = InterestedToSell.objects.all()


class GeneralCallViewSet(viewsets.ModelViewSet):
    serializer_class = GeneralCallSerializer
    permisson_classes = [permissions.IsAuthenticated]
    queryset = GeneralCall.objects.all()


class CustomerInteractionPostPaidViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerInteractionPostPaidSerializer
    permisson_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "=ticket_number",
        "=apn",
        "caller_full_name",
        "=caller_phone",
        "=email",
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
            qs = CustomerInteractionPostPaid.objects.select_related("company").filter(
                company__client__user__in=user
            )
            return qs
        elif current_user.designation_category == "staff":
            qs = CustomerInteractionPostPaid.objects.all()
            return qs
        elif current_user.is_superuser:
            qs = CustomerInteractionPostPaid.objects.filter(
                ticket_number__icontains="PSCI"
            )
            return qs


class CreateCustomerInteractionPostPaidComment(generics.CreateAPIView):
    serializer_class = CustomerInteractionPostPaidCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomerInteractionPostPaidComment.objects.select_related(
        "customer_interaction_post_paid", "user"
    ).all()

    def perform_create(self, serializer):
        user = self.request.user
        post_paid_cust_interaction_id = self.kwargs.get("id")
        customer_interaction_post_paid = get_object_or_404(
            CustomerInteractionPostPaid, id=post_paid_cust_interaction_id
        )
        comments = CustomerInteractionPostPaidComment.objects.select_related(
            "customer_interaction_post_paid", "user"
        ).filter(customer_interaction_post_paid=customer_interaction_post_paid.id)
        if customer_interaction_post_paid:
            emails = (
                customer_interaction_post_paid.agent.user.email
                + " "
                + customer_interaction_post_paid.company.client.user.email
            )
            emails = emails.split()

            mail.send(
                "postmaster@psalmsglobal.com",
                bcc=emails,
                template="cust_interaction_comment_update",
                context={
                    "interaction": customer_interaction_post_paid,
                    "comments": comments,
                },
            )
        serializer.save(
            user=user, customer_interaction_post_paid=customer_interaction_post_paid
        )
