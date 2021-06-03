from rest_framework import serializers

from apps.callme.models import Company

from apps.prepaid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPrepaid,
    CustomerInteractionPrepaidComment,
)
from apps.authentication.models import Client, Staff


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


class CustomerInteractionPrepaidSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
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

    class Meta:
        model = CustomerInteractionPrepaid
        fields = (
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
            "customer_interaction_prepaid_comments",
        )