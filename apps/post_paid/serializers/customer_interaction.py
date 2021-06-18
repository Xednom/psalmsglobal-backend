from rest_framework import serializers

from apps.callme.models import Company

from apps.post_paid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPostPaid,
    CustomerInteractionPostPaidComment,
    InteractionRecord
)
from apps.authentication.models import Client, Staff


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
            return "Staff"
        else:
            return "Client"


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


class CustomerInteractionPostPaidSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
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

    class Meta:
        model = CustomerInteractionPostPaid
        fields = (
            "id",
            "ticket_number",
            "company",
            "apn",
            "caller_full_name",
            "caller_phone",
            "email",
            "reason_of_the_call",
            "interested_to_sell",
            "interested_to_buy",
            "general_call",
            "total_minutes",
            "crm",
            "leads_transferred_crm",
            "customer_interaction_post_paid_comments",
            "customer_interaction_post_paid_records"
        )
