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

    def get_queryset(self):
        current_user = self.request.user
        user_company = Company.objects.select_related("client").filter(
            client__user=current_user
        )

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = CustomerInteractionPostPaid.objects.select_related("company").filter(
                company=user_company
            )
            return qs
        elif current_user.is_superuser:
            qs = CustomerInteractionPostPaid.objects.all()
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
        job_order = get_object_or_404(
            CustomerInteractionPostPaidComment, id=post_paid_cust_interaction_id
        )
        serializer.save(user=user, job_order_category=job_order)