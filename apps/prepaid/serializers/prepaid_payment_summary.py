from rest_framework import serializers

from apps.prepaid.models import PaymentSummary
from apps.authentication.models import Client


__all__ = ("PaymentSummarySerializer",)


class PaymentSummarySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = PaymentSummary
        fields = (
            "client",
            "date_purchase",
            "total_amount_paid",
            "total_converted_minutes",
            "notes",
        )
