from rest_framework import serializers

from apps.post_paid.models import InteractionRecord
from apps.authentication.models import Client, Staff


__all__ = ("InteractionRecordSerializer",)


class InteractionRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    agent_name = serializers.SerializerMethodField()
    agent_code = serializers.SerializerMethodField()

    class Meta:
        model = InteractionRecord
        fields = (
            "id",
            "client",
            "agent",
            "agent_code",
            "agent_name",
            "date_called",
            "ticket_number",
            "total_minutes",
            "summary",
            "customer_interaction_post_paid",
        )
    
    def get_agent_name(self, instance):
        return f"{instance.agent.staff_name}"
    
    def get_agent_code(self, instance):
        return f"{instance.agent.staff_id}"
