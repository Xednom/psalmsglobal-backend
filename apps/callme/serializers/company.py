from rest_framework import serializers

from apps.callme.models import Company, Crm
from apps.authentication.models import Client


__all__ = ("CompanySerializer",)


class CompanySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    company_crm = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            "id",
            "client",
            "company_crm",
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
    
    def get_company_crm(self, instance):
        company_crm = Crm.objects.filter(company=instance.id)
        company_crm = [company_crm.crm for company_crm in company_crm.all()]
        return company_crm
