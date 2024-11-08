from post_office import mail

from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.prepaid.models import (
    JobOrderPrepaid,
    CustomerInteractionPrepaid,
    JobOrderCommentPrepaid,
)
from apps.authentication.models import Client, Staff


User = get_user_model()


__all__ = ("JobOrderPrepaidSerializer", "JobOrderCommentSerializer")


class JobOrderCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderCommentPrepaid
        fields = ("id", "job_order", "user", "comment", "commenter", "created_at")

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            user = User.objects.filter(username=instance.user)
            staffs = Staff.objects.select_related("user").filter(user__in=user)
            staff_code = [staff.staff_id for staff in staffs]
            return "".join(staff_code)
        elif instance.user.designation_category != "staff":
            user = User.objects.filter(username=instance.user)
            clients = Client.objects.select_related("user").filter(user__in=user)
            client_code = [client.client_code for client in clients]
            return "".join(client_code)


class JobOrderPrepaidSerializer(serializers.ModelSerializer):
    caller_interaction_record = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=CustomerInteractionPrepaid.objects.all(),
        allow_null=True,
        required=False,
    )
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )
    prepaid_job_order_comments = JobOrderCommentSerializer(
        many=True, required=False, allow_null=True
    )
    agent_code = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderPrepaid
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
            "prepaid_job_order_comments",
        )

    def get_agent_code(self, instance):
        agent_codes = [agent.staff_id for agent in instance.va_assigned.all()]
        agent_codes = ", ".join(agent_codes)
        return agent_codes

    def create(self, validated_data):
        instance = super(JobOrderPrepaidSerializer, self).create(validated_data)
        emails = instance.client_email + " " + instance.staff_email
        mail.send(
            "postmaster@psalmsglobal.com",
            bcc=emails.split(),
            template="job_order_create",
            context={"job_order": instance},
        )
        return instance
