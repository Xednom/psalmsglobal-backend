from rest_framework import serializers

from apps.vodaconnect.models import OtherCharge
from apps.authentication.models import Client


__all__ = ("OtherChargeSerializer",)


class OtherChargeSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = OtherCharge
        fields = (
            "date",
            "client",
            "vodaconnect_number",
            "type_charge",
            "amount",
            "payment_reference",
            "payment_status",
            "notes",
        )
