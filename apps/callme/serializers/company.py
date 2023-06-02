from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.callme.models import Company, Crm
from apps.authentication.models import Client


User = get_user_model()


__all__ = ("CompanySerializer",)


class CompanySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    company_crm = serializers.SerializerMethodField()
    company_client_code = serializers.SerializerMethodField()
    company_client_account_type = serializers.SerializerMethodField()
    company_client_sub_category = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            "id",
            "client",
            "company_crm",
            "company_client_code",
            "company_client_account_type",
            "company_owner_name",
            "company_name",
            "business_type",
            "company_phone",
            "company_email",
            "company_complete_address",
            "company_forwarding_email",
            "paypal_email",
            "notes",
            "company_client_sub_category"
        )

    def get_company_crm(self, instance):
        company_crm = Crm.objects.filter(company=instance.id)
        company_crm = [company_crm.crm for company_crm in company_crm.all()]
        return company_crm

    def get_company_client_code(self, instance):
        client_codes = Client.objects.filter(client_code=instance.client.client_code)
        client_code = [client_code.client_code for client_code in client_codes.all()]
        client_code = "".join(client_code)
        return client_code

    def get_company_client_account_type(self, instance):
        client_account_types = User.objects.filter(username=instance.client.user)
        client_account_type = [
            client.account_type for client in client_account_types.all()
        ]
        client_account_type = "".join(client_account_type)
        return client_account_type

    def get_company_client_sub_category(self, instance):
        clients = User.objects.filter(username=instance.client.user)
        client_sub_category = [
            client.sub_category for client in clients.all()
        ]
        client_sub_category = "".join(client_sub_category)
        return client_sub_category
