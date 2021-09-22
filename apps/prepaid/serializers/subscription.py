from django.db.models.query import QuerySet
from rest_framework import serializers

from apps.prepaid.models import SubscriptionInfo, PrepaidSubscription, PlanType
from apps.authentication.models import Client
from apps.callme.models import Company, company


__all__ = ("SubscriptionInfoSerializer", "PrepaidSubscriptionSerializer")


class SubscriptionInfoSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = SubscriptionInfo
        fields = (
            "company",
            "signed_up_date",
            "signed_out_date",
            "date_of_subscription_starts",
            "status",
            "script_created",
            "notes",
        )


class PrepaidSubscriptionSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    plan_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=PlanType.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = PrepaidSubscription
        fields = (
            "client",
            "date_paid",
            "month_year",
            "plan_type",
            "monthly_fee",
            "payment_status",
            "payment_reference",
            "notes",
        )
