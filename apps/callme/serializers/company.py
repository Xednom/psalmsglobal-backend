from rest_framework import serializers

from apps.callme.models import Company
from apps.authentication.models import Client


__all__ = ("CompanySerializer",)


class CompanySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Company
        fields = (
            "id",
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
