from rest_framework import serializers

from apps.prepaid.models import AccountBalance
from apps.authentication.models import Client


__all__ = ("AccountBalanceSerializer",)


class AccountBalanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = AccountBalance
        fields = (
            "client",
            "account_total_aquired_minutes",
            "account_total_mins_used",
            "account_total_mins_unused",
        )
