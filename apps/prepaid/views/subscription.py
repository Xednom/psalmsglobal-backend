from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import Company
from apps.prepaid.models import SubscriptionInfo, PrepaidSubscription
from apps.prepaid.serializers import SubscriptionInfoSerializer, PrepaidSubscriptionSerializer

User = get_user_model()


__all__ = ("SubscriptionInfoViewSet", "PrepaidSubscriptionViewSet")


class SubscriptionInfoViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionInfoSerializer
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
            qs = SubscriptionInfo.objects.select_related("company").filter(
                company=user_company
            )
            return qs
        elif current_user.is_superuser:
            qs = SubscriptionInfo.objects.all()
            return qs


class PrepaidSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = PrepaidSubscriptionSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = PrepaidSubscription.objects.select_related("client").filter(client=user)
            return qs
        elif current_user.is_superuser:
            qs = PrepaidSubscription.objects.all()
            return qs
