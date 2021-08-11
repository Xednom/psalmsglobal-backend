from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth import get_user_model

from apps.callme.models import Company, Form

from apps.post_paid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPostPaid,
    CustomerInteractionPostPaidComment,
    InteractionRecord,
    JobOrderPostPaid,
)
from apps.authentication.models import Client, Staff
from apps.callme.serializers import AttributeSerializer, FormSerializer

User = get_user_model()


__all__ = (
    "InterestedToSellSerializer",
    "InterestedToBuySerializer",
    "GeneralCallSerializer",
    "CustomerInteractionPostPaidCommentSerializer",
    "CustomerInteractionPostPaidSerializer",
)


class InterestedToSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedToSell
        fields = ("name",)


class InterestedToBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedToBuy
        fields = ("name",)


class GeneralCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCall
        fields = ("name",)


class CustomerInteractionPostPaidCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CustomerInteractionPostPaidComment
        fields = (
            "customer_interaction_post_paid",
            "user",
            "comment",
            "commenter",
            "created_at",
        )

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


class CustomerInteractionPostPaidRecordSerializer(serializers.ModelSerializer):
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
            "client",
            "agent",
            "agent_code",
            "agent_name",
            "date_called",
            "ticket_number",
            "total_minutes",
            "summary",
        )

    def get_agent_name(self, instance):
        return f"{instance.agent.staff_name}"

    def get_agent_code(self, instance):
        return f"{instance.agent.staff_id}"


class JobOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOrderPostPaid
        fields = (
            "caller_interaction_record",
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


class CustomerInteractionPostPaidSerializer(WritableNestedModelSerializer):
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
    customer_interaction_post_paid_comments = (
        CustomerInteractionPostPaidCommentSerializer(
            many=True, required=False, allow_null=True
        )
    )
    customer_interaction_post_paid_records = (
        CustomerInteractionPostPaidRecordSerializer(
            many=True, required=False, allow_null=True
        )
    )
    customer_interaction_post_paid_forms = FormSerializer(
        many=True, required=False, allow_null=True
    )
    interaction_job_orders = JobOrderSerializer(
        many=True, required=False, allow_null=True
    )

    class Meta:
        model = CustomerInteractionPostPaid
        fields = (
            "id",
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
            "script_answer",
            "leads_transferred_crm",
            "customer_interaction_post_paid_comments",
            "customer_interaction_post_paid_records",
            "customer_interaction_post_paid_forms",
            "interaction_job_orders",
        )

    def get_company_client(self, instance):
        return f"{instance.company.client.id}"

    def get_company_crm(self, instance):
        company_crm = [
            company_crm.crm for company_crm in instance.company.company_crms.all()
        ]
        return company_crm
