from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.post_paid.models import AccountCharge
from apps.post_paid.serializers import AccountChargeSerializer

User = get_user_model()


__all__ = ("AccountChargeViewSet",)


class AccountChargeViewSet(viewsets.ModelViewSet):
    serializer_class = AccountChargeSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = AccountCharge.objects.select_related("client").filter(client=user)
            return qs
        elif current_user.is_superuser:
            qs = AccountCharge.objects.all()
            return qs
