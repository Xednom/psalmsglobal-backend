from rest_framework import serializers

from apps.prepaid.models import Prepaid, SubscriptionType
from apps.authentication.models import Client


__all__ = ("PrepaidSerializer",)


class PrepaidSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    subscription_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=SubscriptionType.objects.all(),
        required=False,
        allow_null=True,
    )
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Prepaid
        fields = (
            "id",
            "client",
            "subscription_type",
            "monthly_fees",
            "start_of_subscription",
            "end_of_subscription",
            "account_status",
            "notes",
            "client_name"
        )
    
    def get_client_name(self, instance):
        return f"{instance.client.user.first_name} {instance.client.user.last_name}"
