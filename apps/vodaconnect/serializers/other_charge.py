from rest_framework import serializers

from apps.vodaconnect.models import OtherCharge
from apps.authentication.models import Client


__all__ = ("OtherChargeSerializer",)


class OtherChargeSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    client_name = serializers.CharField(source="client.user.user_full_name", read_only=True)

    class Meta:
        model = OtherCharge
        fields = (
            "id",
            "date",
            "client",
            "client_name",
            "vodaconnect_number",
            "type_charge",
            "amount",
            "payment_reference",
            "payment_status",
            "notes",
        )
