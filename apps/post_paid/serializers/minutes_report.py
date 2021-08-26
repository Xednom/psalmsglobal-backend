from rest_framework import serializers

from apps.post_paid.models import MinutesReport
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
            "plan_type",
            "cost_of_plan",
            "plan_allocated_minutes",
            "ci_minutes_overview",
            "general_request_total_minutes",
            "monthly_usage",
            "total_minutes_unused",
        )
