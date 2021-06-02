from rest_framework import serializers

from apps.post_paid.models import PostPaid
from apps.authentication.models import Client


__all__ = ("PostPaidSerializer",)


class PostPaidSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = PostPaid
        fields = (
            "client",
            "plan_type",
            "total_minutes",
            "cost_of_plan",
            "start_of_plan",
            "end_of_plan",
            "account_status",
            "recurring_bill",
            "notes"
        )
