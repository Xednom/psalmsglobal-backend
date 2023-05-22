from rest_framework import serializers

from apps.post_paid.models import (
    InteractionRecord,
    CustomerInteractionPostPaid,
    TicketSummaryRecord,
    TicketSummary,
)
from apps.authentication.models import Client, Staff


__all__ = ("InteractionRecordSerializer", "TicketSummaryInteractionRecordSerializer")


class InteractionRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    customer_interaction_post_paid = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=CustomerInteractionPostPaid.objects.all(),
        required=False,
        allow_null=True,
    )
    agent_name = serializers.CharField(source="agent.staff_name")
    agent_code = serializers.CharField(source="agent.staff_id")

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
            "customer_interaction_post_paid",
        )


class TicketSummaryInteractionRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    ticket_summary = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=TicketSummary.objects.all(),
        required=False,
        allow_null=True,
    )
    agent_name = serializers.CharField(source="agent.staff_name")
    agent_code = serializers.CharField(source="agent.staff_id")

    class Meta:
        model = TicketSummaryRecord
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
            "ticket_summary",
        )
