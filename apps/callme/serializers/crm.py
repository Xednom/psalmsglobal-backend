from apps.callme import models
from rest_framework import serializers

from apps.callme.models import Crm


__all__ = ("CrmSerializer",)


class CrmSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Crm.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Crm
        fields = (
            "company",
            "crm",
            "type_of_crm",
            "crm_url",
            "crm_login",
            "notes"
        )