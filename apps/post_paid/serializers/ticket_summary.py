from post_office import mail
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth import get_user_model

from apps.callme.models import Company, Form, Attribute

from apps.post_paid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    TicketSummary,
    TicketSummaryComment,
    TicketSummaryRecord,
    JobOrderTicketSummary,
)
from apps.authentication.models import Client, Staff
from apps.callme.serializers import AttributeSerializer, FormSerializer
from apps.grading.serializers import TicketSummaryRateSerializer

User = get_user_model()


__all__ = ()


class InterestedToBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedToBuy
        fields = ("name",)


class GeneralCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCall
        fields = ("name",)


class TicketSummaryCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = TicketSummaryComment
        fields = (
            "ticket_summary",
            "user",
            "comment",
            "commenter",
            "created_at",
        )

    def get_commenter(self, instance):
        if instance.user:
            if instance.user.designation_category == "current_client":
                user = User.objects.filter(username=instance.user)
                clients = Client.objects.select_related("user").filter(user__in=user)
                client_code = [client.client_code for client in clients]
                return "".join(client_code)
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


class TicketSummaryRecordSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    agent_name = serializers.CharField(
        source="agent.staff_name", default=None, allow_null=True, required=False
    )
    agent_code = serializers.CharField(
        source="agent.staff_id", default=None, allow_null=True, required=False
    )

    class Meta:
        model = TicketSummaryRecord
        fields = (
            "client",
            "agent",
            "agent_code",
            "agent_name",
            "date_called",
            "ticket_number",
            "total_minutes",
            "summary",
        )


class JobOrderTicketSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOrderTicketSummary
        fields = (
            "ticket_summary_job_order",
            "client",
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
        )


class TicketSummarySerializer(WritableNestedModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
    agent = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    company_crm = serializers.SerializerMethodField()
    company_client = serializers.SerializerMethodField()
    interested_to_sell = serializers.SlugRelatedField(
        slug_field="name", queryset=InterestedToSell.objects.all()
    )
    interested_to_buy = serializers.SlugRelatedField(
        slug_field="name", queryset=InterestedToBuy.objects.all()
    )
    general_call = serializers.SlugRelatedField(
        slug_field="name", queryset=GeneralCall.objects.all()
    )
    ticket_summary_comments = TicketSummaryCommentSerializer(
        many=True, required=False, allow_null=True
    )
    ticket_summary_records = (
        TicketSummaryRecordSerializer(
            many=True, required=False, allow_null=True
        )
    )
    ticket_summary_forms = FormSerializer(
        many=True, required=False, allow_null=True
    )
    ticket_summary_job_orders = JobOrderTicketSummarySerializer(
        many=True, required=False, allow_null=True
    )
    client_account_type = serializers.SerializerMethodField()
    ticket_summary_rates = TicketSummaryRateSerializer(
        many=True, required=False, allow_null=True
    )
    client_sub_category = serializers.SerializerMethodField()

    class Meta:
        model = TicketSummary
        fields = (
            "id",
            "created_at",
            "ticket_number",
            "company",
            "agent",
            "company_crm",
            "company_client",
            "apn",
            "reference_number",
            "state",
            "county",
            "address",
            "caller_full_name",
            "caller_phone",
            "email",
            "reason_of_the_call",
            "interested_to_sell",
            "interested_to_buy",
            "general_call",
            "crm",
            "leads_transferred_crm",
            "internal_auditor",
            "ticket_summary_comments",
            "ticket_summary_records",
            "ticket_summary_forms",
            "ticket_summary_job_orders",
            "client_account_type",
            "ticket_summary_rates",
            "client_sub_category",
        )

    def get_company_client(self, instance):
        return f"{instance.company.client.id}"

    def get_company_crm(self, instance):
        company_crm = [
            company_crm.crm for company_crm in instance.company.company_crms.all()
        ]
        return company_crm

    def get_client_account_type(self, instance):
        client_account_types = User.objects.filter(
            username=instance.company.client.user
        )
        client_account_type = [
            client.account_type for client in client_account_types.all()
        ]
        client_account_type = "".join(client_account_type)
        return client_account_type

    def get_client_sub_category(self, instance):
        client_sub_categories = User.objects.filter(
            username=instance.company.client.user
        )
        client_sub_category = [
            client.sub_category for client in client_sub_categories.all()
        ]
        client_sub_category = "".join(client_sub_category)
        return client_sub_category
