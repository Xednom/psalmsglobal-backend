from post_office import mail

from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.post_paid.models import (
    JobOrderPostPaid,
    CustomerInteractionPostPaid,
    JobOrderComment,
    TicketSummary,
    JobOrderTicketSummaryComment,
    JobOrderTicketSummary,
)
from apps.authentication.models import Client, Staff


User = get_user_model()


__all__ = (
    "JobOrderPostPaidSerializer",
    "JobOrderCommentSerializer",
    "JobOrderTicketSummaryCommentSerializer",
    "JobOrderTicketSummarySerializer",
)


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

    def create(self, validated_data):
        instance = super(JobOrderPostPaidSerializer, self).create(validated_data)
        emails = instance.client_email + " " + instance.staff_email
        mail.send(
            "postmaster@psalmsglobal.com",
            bcc=emails.split(),
            template="job_order_create",
            context={"job_order": instance},
        )
        return instance


class JobOrderTicketSummaryCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderTicketSummaryComment
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


class JobOrderTicketSummarySerializer(serializers.ModelSerializer):
    ticket_summary_job_order = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=TicketSummary.objects.all(),
        allow_null=True,
        required=False,
    )
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )
    ticket_summary_job_order_comments = JobOrderTicketSummaryCommentSerializer(
        many=True, required=False, allow_null=True
    )
    agent_code = serializers.SerializerMethodField()
    client_sub_category = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderTicketSummary
        fields = (
            "id",
            "ticket_summary_job_order",
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
            "ticket_summary_job_order_comments",
            "client_sub_category",
        )

    def get_agent_code(self, instance):
        agent_codes = [agent.staff_id for agent in instance.va_assigned.all()]
        agent_codes = ", ".join(agent_codes)
        return agent_codes

    def get_client_sub_category(self, instance):
        if instance.client:
            client_sub_categories = User.objects.filter(
                username=instance.client.user
            )
            client_sub_category = [
                client.sub_category for client in client_sub_categories.all()
            ]
            client_sub_category = "".join(client_sub_category)
            return client_sub_category

    def create(self, validated_data):
        instance = super(JobOrderTicketSummarySerializer, self).create(validated_data)
        emails = instance.client_email + " " + instance.staff_email
        mail.send(
            "postmaster@psalmsglobal.com",
            bcc=emails.split(),
            template="job_order_create",
            context={"job_order": instance},
        )
        return instance
