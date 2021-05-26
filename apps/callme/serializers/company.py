from rest_framework import serializers

from apps.callme.models import Company


__all__ = ("CompanySerializer",)


class CompanySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Company
        fields = (
            "client",
            "company_owner_name",
            "company_name",
            "business_type",
            "company_phone",
            "company_email",
            "company_complete_address",
            "company_forwarding_email",
            "paypal_email",
            "notes"
        )
