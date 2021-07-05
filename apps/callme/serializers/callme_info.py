from rest_framework import serializers

from apps.callme.models import CallMeInfo


__all__ = ("CallMeInfoSerializer",)


class CallMeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallMeInfo
        fields = (
            "id",
            "company",
            "apn",
            "reference",
            "short_legal_description",
            "property_address",
            "property_city",
            "property_county",
            "property_state",
            "property_zip",
            "first_name",
            "last_name",
            "company_name",
            "buyer_offer_amount",
            "approved_option_amount",
            "other_terms",
            "seller_offer_amount",
            "other_offer_terms",
            "notes",
            "offer_status",
            "offer_status_notes",
        )