from apps.callme import models
from rest_framework import serializers

from apps.callme.models import Crm, Company


__all__ = ("CrmSerializer",)


class CrmSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
    client_code = serializers.CharField(
        source="company.client.client_code", required=False, allow_null=True
    )

    class Meta:
        model = Crm
        fields = (
            "id",
            "company",
            "client_code",
            "crm",
            "type_of_crm",
            "crm_url",
            "crm_login",
            "notes",
        )
