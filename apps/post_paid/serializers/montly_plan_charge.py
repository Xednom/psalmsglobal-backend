from rest_framework import serializers

from apps.post_paid.models import MonthlyCharge
from apps.authentication.models import Client


__all__ = ("MonthlyChargeSerializer",)


class MonthlyChargeSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = MonthlyCharge
        fields = (
            "client",
            "month_year",
            "total_minutes",
            "plan_type",
            "cost_of_plan",
            "payment_status",
            "payment_reference",
            "notes"
        )
