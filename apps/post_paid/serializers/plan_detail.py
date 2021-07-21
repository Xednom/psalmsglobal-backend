from rest_framework import serializers

from apps.post_paid.models import PostPaid, PlanType, CostPlan
from apps.authentication.models import Client


__all__ = ("PostPaidSerializer", "PlanTypeSerializer", "CostPlanSerializer")


class PlanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanType
        fields = ("name",)


class CostPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostPlan
        fields = ("name",)


class PostPaidSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    client_name = serializers.SerializerMethodField()
    plan_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=PlanType.objects.all(),
        required=False,
        allow_null=True,
    )
    cost_of_plan = serializers.SlugRelatedField(
        slug_field="name",
        queryset=CostPlan.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = PostPaid
        fields = (
            "id",
            "client",
            "client_name",
            "plan_type",
            "total_minutes",
            "cost_of_plan",
            "start_of_plan",
            "end_of_plan",
            "account_status",
            "recurring_bill",
            "notes",
        )

    def get_client_name(self, instance):
        return instance.client.client_name
