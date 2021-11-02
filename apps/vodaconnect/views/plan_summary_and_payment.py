from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.vodaconnect.models import PlanSummaryAndPayment
from apps.vodaconnect.serializers import PlanSummaryAndPaymentSerializer

User = get_user_model()


__all__ = ("PlanSummaryAndPaymentViewSet",)


class PlanSummaryAndPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSummaryAndPaymentSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = PlanSummaryAndPayment.objects.select_related("client").filter(
                client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = PlanSummaryAndPayment.objects.select_related("client").all()
            return qs
