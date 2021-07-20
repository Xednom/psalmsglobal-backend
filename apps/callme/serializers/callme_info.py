from rest_framework import serializers

from apps.callme.models import Company, PropertyInfo, OfferStatus, PropertyFileInfo


__all__ = ("CallMeInfoSerializer", "OfferStatusSerializer", "PropertyFileSerializer")


class OfferStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferStatus
        fields = ("name",)


class CallMeInfoSerializer(serializers.ModelSerializer):
    offer_status = serializers.SlugRelatedField(
        slug_field="name",
        queryset=OfferStatus.objects.all(),
        allow_null=True,
        required=False,
    )
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True
    )
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


class PropertyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFileInfo
        fields = ("file",)
