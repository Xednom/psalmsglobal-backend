from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.post_paid.models import (
    JobOrderPostPaid,
    CustomerInteractionPostPaid,
    JobOrderComment,
)
from apps.authentication.models import Client, Staff


User = get_user_model()


__all__ = ("JobOrderPostPaidSerializer", "JobOrderCommentSerializer")


class JobOrderCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderComment
        fields = ("job_order", "user", "comment", "commenter", "created_at")

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            user = User.objects.filter(username=instance.user)
            staffs = Staff.objects.select_related("user").filter(user__in=user)
            staff_code = [staff.staff_id for staff in staffs]
            return "".join(staff_code)
        else:
            user = User.objects.filter(username=instance.user)
            clients = Client.objects.select_related("user").filter(user__in=user)
            client_code = [client.client_code for client in clients]
            return "".join(client_code)


class JobOrderPostPaidSerializer(serializers.ModelSerializer):
    caller_interaction_record = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=CustomerInteractionPostPaid.objects.all(),
        allow_null=True,
        required=False,
    )
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )
    job_order_comments = JobOrderCommentSerializer(
        many=True, required=False, allow_null=True
    )
    agent_code = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderPostPaid
        fields = (
            "id",
            "caller_interaction_record",
            "client",
            "agent_code",
            "client_file",
            "client_email",
            "va_assigned",
            "staff_email",
            "ticket_number",
            "request_date",
            "due_date",
            "job_title",
            "job_description",
            "client_notes",
            "va_notes",
            "management_notes",
            "status",
            "date_completed",
            "total_time_consumed",
            "url_of_the_completed_jo",
            "job_order_comments",
        )
    
    def get_agent_code(self, instance):
        agent_codes = [agent.staff_id for agent in instance.va_assigned.all()]
        agent_codes = ", ".join(agent_codes)
        return agent_codes
