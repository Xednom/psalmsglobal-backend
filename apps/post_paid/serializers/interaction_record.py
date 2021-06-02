from rest_framework import serializers

from apps.post_paid.models import InteractionRecord
from apps.authentication.models import Client, Staff


__all__ = ("AccountChargeSerializer",)


class InteractionRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = InteractionRecord
        fields = (
            "client",
            "agent",
            "date_called",
            "total_minutes",
            "summary",
        )
