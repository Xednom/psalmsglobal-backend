from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import Company
from apps.post_paid.models import Subscription
from apps.post_paid.serializers import SubscriptionSerializer

User = get_user_model()


__all__ = ("SubscriptionViewSet",)


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user_company = Company.objects.select_related("client").filter(client__user=current_user)

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Subscription.objects.select_related("company").filter(company=user_company)
            return qs