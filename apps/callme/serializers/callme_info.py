from rest_framework import serializers

from apps.callme.models import PropertyInfo


__all__ = ("CallMeInfoSerializer",)


class CallMeInfoSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = PropertyInfo
        fields = (
            "id",
            "company",
            "company_name",
            "apn",
            "reference",
            "short_legal_description",
            "property_address",
            "property_city",
            "property_county",
            "property_state",
            "property_zip",
            "full_name",
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

    def get_company_name(self, instance):
        return f"{instance.company.company_name}"
