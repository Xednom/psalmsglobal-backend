from django.contrib.auth import get_user, get_user_model

from rest_framework import generics, viewsets, permissions, filters
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client
from apps.callme.models import Company
from apps.prepaid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPrepaid,
    CustomerInteractionPrepaidComment,
)
from apps.prepaid.serializers import (
    InterestedToSellSerializer,
    InterestedToBuySerializer,
    GeneralCallSerializer,
    CustomerInteractionPrepaidCommentSerializer,
    CustomerInteractionPrepaidSerializer,
)

User = get_user_model()


__all__ = (
    "InterestedToBuyViewSet",
    "InterestedToSellViewSet",
    "GeneralCallViewSet",
    "CustomerInteractionPrepaidViewSet",
    "CreateCustomerInteractionPrepaidComment",
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


class CustomerInteractionPrepaidViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerInteractionPrepaidSerializer
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
            qs = CustomerInteractionPrepaid.objects.select_related("company").filter(
                company=user_company
            )
            return qs
        elif current_user.is_superuser:
            qs = CustomerInteractionPrepaid.objects.all()
            return qs


class CreateCustomerInteractionPrepaidComment(generics.CreateAPIView):
    serializer_class = CustomerInteractionPrepaidCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomerInteractionPrepaidComment.objects.select_related(
        "customer_interaction_prepaid", "user"
    ).all()

    def perform_create(self, serializer):
        user = self.request.user
        prepaid_cust_interaction_id = self.kwargs.get("id")
        customer_interaction = get_object_or_404(
            CustomerInteractionPrepaidComment, id=prepaid_cust_interaction_id
        )
        serializer.save(user=user, customer_interaction_prepaid=customer_interaction)
