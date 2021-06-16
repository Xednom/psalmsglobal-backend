from rest_framework import serializers

from apps.callme.models import Company

from apps.post_paid.models import (
    InterestedToSell,
    InterestedToBuy,
    GeneralCall,
    CustomerInteractionPostPaid,
    CustomerInteractionPostPaidComment,
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
    class Meta:
        model = CustomerInteractionPostPaidComment
        fields = ("customer_interaction_post_paid", "user", "comment")


class CustomerInteractionPostPaidSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(slug_field="company_name",
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
    customer_interaction_post_paid_comments = (
        CustomerInteractionPostPaidCommentSerializer(
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
        )
