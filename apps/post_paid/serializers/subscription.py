from rest_framework import serializers

from apps.post_paid.models import Subscription


__all__ = ("SubscriptionSerializer",)


class SubscriptionSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Subscription.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Subscription
        fields = (
            "company",
            "signed_up_date",
            "signed_out_date",
            "billing_cycle",
            "date_call_started",
            "status",
            "script_created",
            "notes",
        )
