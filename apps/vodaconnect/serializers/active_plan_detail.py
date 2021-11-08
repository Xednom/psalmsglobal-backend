from django.db.models.query import QuerySet
from rest_framework import serializers

from apps.vodaconnect.models import ActivePlanDetail, PlanType
from apps.authentication.models import Client


__all__ = ("ActivePlanDetailSerialize",)


class ActivePlanDetailSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    plan_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=PlanType.objects.all(),
        required=False,
        allow_null=True,
    )

    client_name = serializers.CharField(source="client.user.user_full_name")

    class Meta:
        model = ActivePlanDetail
        fields = (
            "id",
            "client",
            "client_name",
            "plan_type",
            "total_minutes_included",
            "cost_of_plan",
            "start_of_plan",
            "end_of_plan",
            "account_status",
            "recurring_bill",
        )
