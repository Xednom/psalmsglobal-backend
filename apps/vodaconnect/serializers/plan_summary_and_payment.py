from rest_framework import serializers

from apps.vodaconnect.models import PlanSummaryAndPayment
from apps.authentication.models import Client


__all__ = ("PlanSummaryAndPaymentSerializer",)


class PlanSummaryAndPaymentSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    client_name = serializers.CharField(
        source="client.user.user_full_name", read_only=True
    )

    class Meta:
        model = PlanSummaryAndPayment
        fields = (
            "id",
            "created_at",
            "client",
            "client_name",
            "month_year",
            "plan_type",
            "total_minutes",
            "cost_of_plan",
            "payment_reference",
            "status",
            "date_of_paid",
        )
