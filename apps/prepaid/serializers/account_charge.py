from rest_framework import serializers

from apps.prepaid.models import AccountCharge
from apps.authentication.models import Client, Staff


__all__ = ("AccountChargeSerializer",)


class AccountChargeSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = AccountCharge
        fields = (
            "client",
            "agent",
            "ticket_number",
            "date_called",
            "total_minutes",
            "notes",
        )
