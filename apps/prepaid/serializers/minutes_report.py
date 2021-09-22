from rest_framework import serializers

from apps.prepaid.models import MinutesReport
from apps.authentication.models import Client


__all__ = ("MinutesReportSerializer",)


class MinutesReportSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = MinutesReport
        fields = (
            "client",
            "month_year",
            "customer_interaction_mins_overview",
            "general_request_mins_overview",
            "consumed_minutes",
        )
