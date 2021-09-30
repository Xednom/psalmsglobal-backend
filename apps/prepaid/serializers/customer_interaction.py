from django.contrib.auth import get_user_model

from post_office import mail
from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.callme.models import Company, Form, Attribute
from apps.post_paid.models import InterestedToSell, InterestedToBuy, GeneralCall
from apps.prepaid.models import (
    CustomerInteractionPrepaid,
    CustomerInteractionPrepaidComment,
)
from apps.authentication.models import Client, Staff

from apps.callme.serializers import FormSerializer


User = get_user_model()


__all__ = (
    "InterestedToSellSerializer",
    "InterestedToBuySerializer",
    "GeneralCallSerializer",
    "CustomerInteractionPrepaidCommentSerializer",
    "CustomerInteractionPrepaidSerializer",
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


class CustomerInteractionPrepaidCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInteractionPrepaidComment
        fields = ("customer_interaction_prepaid", "user", "comment")


class CustomerInteractionPrepaidSerializer(WritableNestedModelSerializer):
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
    customer_interaction_prepaid_comments = (
        CustomerInteractionPrepaidCommentSerializer(
            many=True, required=False, allow_null=True
        )
    )
    customer_interaction_prepaid_forms = FormSerializer(
        many=True, required=False, allow_null=True
    )
    client_account_type = serializers.SerializerMethodField()
    company_client = serializers.SerializerMethodField()
    company_crm = serializers.SerializerMethodField()

    class Meta:
        model = CustomerInteractionPrepaid
        fields = (
            "id",
            "ticket_number",
            "company",
            "apn",
            "reference_number",
            "county",
            "state",
            "address",
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
            "customer_interaction_prepaid_forms",
            "customer_interaction_prepaid_comments",
            "client_account_type",
            "company_client",
            "company_crm",
        )

    def get_company_client(self, instance):
        return f"{instance.company.client.id}"
    
    def get_company_crm(self, instance):
        company_crm = [
            company_crm.crm for company_crm in instance.company.company_crms.all()
        ]
        return company_crm
    
    def get_client_account_type(self, instance):
        client_account_types = User.objects.filter(username=instance.company.client.user)
        client_account_type = [client.account_type for client in client_account_types.all()]
        client_account_type = "".join(client_account_type)
        return client_account_type
