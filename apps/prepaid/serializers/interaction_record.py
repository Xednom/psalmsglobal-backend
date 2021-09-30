from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.prepaid.models import InteractionRecord, CustomerInteractionPrepaid
from apps.authentication.models import Client, Staff


User = get_user_model()


__all__ = ("InteractionRecordSerializer",)


class InteractionRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    customer_interaction_prepaid = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=CustomerInteractionPrepaid.objects.all(),
        required=False,
        allow_null=True,
    )
    agent_name = serializers.SerializerMethodField()
    agent_code = serializers.SerializerMethodField()
    client_account_type = serializers.SerializerMethodField()

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
            "status",
            "client_feedback_status",
            "dispute_details",
            "other_feedback",
            "client_notes",
            "internal_management_ticket_status",
            "memo_solution_from_the_mgmt",
            "other_ticket_status",
            "customer_interaction_prepaid",
            "client_account_type",
        )

    def get_client_account_type(self, instance):
        if instance.client:
            client_account_types = User.objects.filter(username=instance.client.user)
            client_account_type = [client.account_type for client in client_account_types.all()]
            client_account_type = "".join(client_account_type)
            return client_account_type

    def get_agent_name(self, instance):
        return f"{instance.agent.staff_name}"

    def get_agent_code(self, instance):
        return f"{instance.agent.staff_id}"
