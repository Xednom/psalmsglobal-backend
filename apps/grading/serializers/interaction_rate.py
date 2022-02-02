from rest_framework import serializers

from apps.post_paid.models import CustomerInteractionPostPaid
from apps.prepaid.models import CustomerInteractionPrepaid
from apps.grading.models import PostpaidInteractionRate, PrepaidInteractionRate
from apps.authentication.models import Client


__all__ = ("PostpaidInteractionRateSerializer", "PrepaidInteractionRateSerializer")


class PostpaidInteractionRateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    post_paid = serializers.PrimaryKeyRelatedField(
        queryset=CustomerInteractionPostPaid.objects.all()
    )

    class Meta:
        model = PostpaidInteractionRate
        fields = (
            "id",
            "post_paid",
            "rating",
            "comment",
            "client",
        )


class PrepaidInteractionRateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    prepaid = serializers.PrimaryKeyRelatedField(
        queryset=CustomerInteractionPrepaid.objects.all()
    )

    class Meta:
        model = PrepaidInteractionRate
        fields = (
            "id",
            "prepaid",
            "rating",
            "comment",
            "client",
        )
