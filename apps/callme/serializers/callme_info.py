from rest_framework import serializers

from apps.callme.models import Company, PropertyInfo, OfferStatus, PropertyFileInfo


__all__ = ("CallMeInfoSerializer", "OfferStatusSerializer", "PropertyFileSerializer")


class OfferStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferStatus
        fields = ("name",)


class CallMeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyInfo
        fields = (
            "client_code",
            "full_name",
            "company_name",
            "reference_number",
            "apn",
            "county",
            "state",
            "size",
            "address",
            "price",
            "due_diligence",
            "ad_content",
            "images",
            "website",
            "comment_offer_tab_customer",
            "comment_offer_tab_client",
            "comment_sales_agent_notes",
            "facebook",
            "fb_groups",
            "landmodo",
            "fsbo",
            "instagram",
            "land_listing",
            "land_flip",
            "land_hub",
            "land_century",
        )


class PropertyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFileInfo
        fields = ("file",)
