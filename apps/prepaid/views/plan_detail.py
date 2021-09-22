from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.prepaid.models import Prepaid
from apps.prepaid.serializers import PrepaidSerializer

User = get_user_model()


__all__ = ("PrepaidViewSet",)


class PrepaidViewSet(viewsets.ModelViewSet):
    serializer_class = PrepaidSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Prepaid.objects.select_related("client", "subscription_type").filter(
                client=user
            )
            return qs
        elif current_user.is_superuser:
            qs = Prepaid.objects.all()
            return qs
